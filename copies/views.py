from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsUserCollaborator
from books.models import Book
from .models import Copy, Borrowings
from .serializers import CopySerializer, BorrowingsSerializer
from django.shortcuts import get_object_or_404
""" from users.models import User
from datetime import datetime, timedelta """


class CopyView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsUserCollaborator]

    serializer_class = CopySerializer
    lookup_url_kwarg = "book_id"

    def get_queryset(self):
        obj_book = get_object_or_404(Book, pk=self.kwargs["book_id"])
        return Copy.objects.filter(book=obj_book)


class CopyDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsUserCollaborator]

    queryset = Copy.objects.all()
    serializer_class = CopySerializer

    lookup_url_kwarg = "copy_id"

    def perform_destroy(self, instance: Copy):
        if instance.state == "Danificado":
            instance.is_available = False
            instance.save()


class BorrowingsView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsUserCollaborator]

    serializer_class = BorrowingsSerializer
    queryset = Borrowings.objects.all()

    """ def perform_create(self, serializer):


        return serializer.save(copy_id=obj_copy, user_id=obj_user, estimated_return_date=estimated_return_date) """


class BorrowingsDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsUserCollaborator]

    serializer_class = BorrowingsSerializer
    lookup_url_kwarg = "borrowing_id"
