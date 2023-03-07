from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer


class BookView(generics.ListCreateAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # def get_queryset(self):
    #     if self.request.user.is_seperuser:
    #         return Book.objects.all()

    #     return Book.objects.filter(
    #         is_active = True
    #     )

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    lookup_url_kwarg = "book_id"

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
