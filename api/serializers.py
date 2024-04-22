from rest_framework import serializers
from PIL import Image
import io

class ImageUploadSerializer(serializers.Serializer):
    image = serializers.ImageField()

    def create(self, validated_data):
        image = validated_data['image']
        return image
