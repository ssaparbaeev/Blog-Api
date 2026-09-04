from rest_framework import serializers
from .models import PostModel
from django.contrib.auth import get_user_model


class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = (
            "id",
            "author",
            "title",
            "body",
            "created_at",
        )


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "username",)
