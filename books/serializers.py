from copies.models import Copy
from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Book, Following


class BookSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        book_obj = Book.objects.create(**validated_data)

        copy_obj = [
            Copy(book=book_obj) for _ in range(book_obj.quantity)
        ]

        Copy.objects.bulk_create(copy_obj)

        return book_obj
    
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
  
    
class FollowingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only= True)
    class Meta:
        model = Following
        fields = [
            "id",
            "book",
            "user",
        ]

        extra_kwargs = {
            "book": {"read_only": True},
            "user": {"read_only": True},
        }

        depth = 1