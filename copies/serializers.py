from rest_framework import serializers
from .models import Copy, Borrowings
from datetime import datetime, timedelta


class CopySerializer(serializers.ModelSerializer):

    class Meta:
        model = Copy
        fields = ["id", "is_available", "state", "book"]
        read_only_fields = ["book"]
        

class BorrowingsSerializer(serializers.ModelSerializer):   

    class Meta:
        model = Borrowings
        fields = ["id", "borrowing_date", "estimated_return_date", "return_date", "copy_id", "user_id"]
        read_only_fields = ["borrowing_date", "estimated_return_date", "return_date"]