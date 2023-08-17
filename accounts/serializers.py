from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("email_verified_at", "date_joined", "last_login",
                   "is_superuser", "is_active", "is_staff", "level",)


class UserRegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "phoneNumber", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
