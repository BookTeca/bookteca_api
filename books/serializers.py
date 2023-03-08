from copies.models import Copy
from rest_framework import serializers
from .models import Book, BookFollowing

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
            "is_active",
            "following"
        ]

        extra_kwargs = {
            "following": {"read_only": True}
        }

    def create(self, validated_data):
        book_obj = Book.objects.create(**validated_data)

        copy_obj = [
            Copy(book=book_obj) for _ in range(book_obj.quantity)
        ]

        Copy.objects.bulk_create(copy_obj)

        return book_obj
    
class BookFollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookFollowing
        fields = [
            "id",
            "book",
            "book_title",
            "user",
            "user_email"
        ]

        extra_kwargs = {
            "book": {"read_only": True},
            "book_title": {"read_only": True},
            "user": {"read_only": True},
            "user_email": {"read_only": True}
        }