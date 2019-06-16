from rest_framework import serializers
from .models import Urls


class UrlsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    short_url = serializers.CharField(
        required=True, allow_blank=False, max_length=7)
    title = serializers.CharField(
        default="", allow_blank=True, max_length=255)
    long_url = serializers.URLField(
        max_length=5000, min_length=None, allow_blank=False)

    def create(self, validated_data):
        """
        Create and return a new `Urls` instance, given the validated data.
        """
        return Urls.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Urls` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance
