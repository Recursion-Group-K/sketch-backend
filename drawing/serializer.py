from rest_framework import serializers
from .models import Drawing
from user.serializer import UserSerializer

class DrawingSerializer(serializers.ModelSerializer):
  user = UserSerializer()
  class Meta:
    model = Drawing
    fields = ['id', 'title', 'image', 'data', 'is_public', 'created_at', 'updated_at', 'user', 'mode'] 