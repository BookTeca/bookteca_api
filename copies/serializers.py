from rest_framework import serializers
from .models import Copy, Loan
from datetime import datetime, timedelta
from books.serializers import BookSerializer
from users.serializers import UserSerializer


class CopySerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = Copy
        fields = ["id", "is_available", "state", "book"]
        read_only_fields = ["book"]


class LoanSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source="user", write_only=True)
    user = UserSerializer(read_only=True)
    copy = CopySerializer(read_only=True)

    def create(self, validated_data: dict) -> Loan:
        obj_copy = validated_data["copy"]
        current_date = datetime.now().date()
        due_date = current_date + timedelta(days=1)

        obj_copy.is_available = False
        obj_copy.book.quantity -= 1
        obj_copy.book.save()
        obj_copy.save()

        if current_date.isoweekday() == 5:
            due_date += timedelta(days=3)

        validated_data["estimated_return_date"] = due_date
        return Loan.objects.create(**validated_data)

    class Meta:
        model = Loan
        fields = ["id", "loan_date", "estimated_return_date", "return_date", "copy", "user", "user_id"]
        read_only_fields = ["loan_date", "estimated_return_date", "return_date", "copy", "user"]
