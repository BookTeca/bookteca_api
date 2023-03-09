from rest_framework import serializers
from .models import Copy, Borrowings
import ipdb
from django.shortcuts import get_object_or_404
from users.models import User
from datetime import datetime, timedelta


class CopySerializer(serializers.ModelSerializer):

    class Meta:
        model = Copy
        fields = ["id", "is_available", "state", "book"]
        read_only_fields = ["book"]


class BorrowingsSerializer(serializers.ModelSerializer):

    def create(self, validated_data: dict) -> Borrowings:
        ipdb.set_trace()
        copy_id = self.data.pop("copy_id", None)
        user_id = self.data.pop("user_id", None)
        obj_copy = get_object_or_404(Copy, pk=copy_id)
        obj_user = get_object_or_404(User, pk=user_id)

        estimated_return_date = datetime.now() + timedelta(days=7)
        validated_data = {copy_id: obj_copy, user_id: obj_user, estimated_return_date: estimated_return_date}

        return Borrowings.objects.create(**validated_data)

    class Meta:
        model = Borrowings
        fields = ["id", "borrowing_date", "estimated_return_date", "return_date", "copy_id", "user_id"]
        read_only_fields = ["borrowing_date", "estimated_return_date", "return_date"]
