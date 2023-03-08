from django.shortcuts import render
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book, BookFollowing
from .serializers import BookSerializer, BookFollowingSerializer


class BookView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

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
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    lookup_url_kwarg = "book_id"

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

class BookFollowingView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = BookFollowing.objects.all()
    serializer_class = BookFollowingSerializer

    lookup_url_kwarg = "book_id"

    def get_queryset(self):
        self.check_object_permissions(self.request, self.request.user)
        if self.request.user.is_superuser:
            return BookFollowing.objects.all()

        return BookFollowing.objects.filter(
            user_email=self.request.user.email
        )

    def perform_create(self, serializer):
        book = Book.objects.get(id=self.kwargs.get("book_id"))
        print(book)
        title = book.title
        email = self.request.user.email
        return serializer.save(user=self.request.user, book=book, book_title=title, user_email=email)