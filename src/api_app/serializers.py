from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Upload


class UploadSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Upload
        fields = ["caption", "image_file"]


class UserSerializer(serializers.ModelSerializer):
    uploads = serializers.PrimaryKeyRelatedField(many=True, queryset=Upload.objects.all())

    class Meta:
        model = User
        fields = ["id", "username", "uploads"]
