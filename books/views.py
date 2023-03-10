from django.shortcuts import render
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from books.permissions import IsColaboratorOrReadyOnly, IsOwnerOrColaboratorOrReadyOnly
from copies.models import Copy
from .models import Book, Following
from .serializers import BookSerializer, FollowingSerializer
from django.core.mail import send_mail


class BookView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsColaboratorOrReadyOnly]

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):

        self.check_object_permissions(self.request, self.request.user)
        if self.request.user.is_superuser:
            return Book.objects.all()

        return Book.objects.filter(
            is_active = True
        )


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrColaboratorOrReadyOnly]

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    lookup_url_kwarg = "book_id"

    def perform_update(self, serializer):
        book = Book.objects.get(pk=self.kwargs.get("book_id"))
        send_mail(
            f"Modificação no livro {book.title}",
            f"Modificação no livro seguido: {self.request.data}",
            None,
            [self.request.user.email],
            fail_silently=False

        )
        serializer.save()
    

    def perform_destroy(self, instance):
        copies_obj = Copy.objects.filter(book_id=self.kwargs.get("book_id"))

        for copie in copies_obj:
            copie.is_available = False
            copie.save()
        
        instance.is_active = False
        instance.save()

class BookFollowingView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrColaboratorOrReadyOnly]
    
    queryset = Following.objects.all()
    serializer_class = FollowingSerializer

    lookup_url_kwarg = "book_id"

    def get_queryset(self):
        self.check_object_permissions(self.request, self.request.user)
        if self.request.user.is_superuser:
            return Following.objects.all()

        return Following.objects.filter(
            user_email=self.request.user.email
        )

    def perform_create(self, serializer):
        book = Book.objects.get(id=self.kwargs.get("book_id"))
        title = book.title
        email = self.request.user.email
        return serializer.save(user=self.request.user, book=book, book_title=title, user_email=email)