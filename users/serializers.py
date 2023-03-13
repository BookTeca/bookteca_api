from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> User:
        super_user = validated_data.pop("is_superuser", None)

        if super_user is True:
            return User.objects.create_superuser(**validated_data)

        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        password = validated_data.pop("password", None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password:
            instance.set_password(password)

        instance.save()

        return instance

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "is_superuser",
            "is_blocked",
            "blocked_until",
            "is_active"
        ]
        extra_kwargs = {
            "password": {"write_only": True}
        }

        read_only_fields = ["is_blocked", "is_active"]
