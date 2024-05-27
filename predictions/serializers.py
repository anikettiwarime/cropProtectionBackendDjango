from rest_framework import serializers
from .models import Prediction

class ImageUploadSerializer(serializers.Serializer):
    image = serializers.ImageField()

class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = ['id', 'image', 'is_intruder', 'created_at']
        read_only_fields = ['created_at']

    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.fingerprint.url
        return request.build_absolute_uri(photo_url)

    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        return None
