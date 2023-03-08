from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsUserCollaborator
from ..books.models import Book
from .models import Copy
from .serializers import CopySerializer
from django.shortcuts import get_object_or_404


class CopyView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsUserCollaborator]

    serializer_class = CopySerializer
    lookup_url_kwarg = "book_id"
    
    def get_queryset(self):
        obj_book = get_object_or_404(Book, pk=self.kwargs["book_id"])
        return Copy.objects.filter(book=obj_book)


class CopyDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsUserCollaborator]

    queryset = Copy.objects.all()
    serializer_class = CopySerializer

    lookup_url_kwarg = "copy_id"

    def perform_destroy(self, instance: Copy):
        if instance.state == "Danificado":
            instance.is_available = False
            instance.save()