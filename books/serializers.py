from copies.models import Copy
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "description",
            "author",
            "published_date",
            "category",
            "quantity",
            "is_active"
        ]

    def create(self, validated_data):
        book_obj = Book.objects.create(**validated_data)

        copy_obj = [
            Copy(book=book_obj) for _ in range(book_obj.quantity)
        ]

        Copy.objects.bulk_create(copy_obj)

        return book_obj