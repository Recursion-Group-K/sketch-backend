from urllib import request
from rest_framework import serializers
from .models import Drawing
from user.models import User
from user.serializer import UserSerializer

class DrawingSerializer(serializers.ModelSerializer):
  user = UserSerializer(read_only=True)
  user_id = serializers.PrimaryKeyRelatedField(
    read_only=True, 
    default=serializers.CurrentUserDefault()
  )
  class Meta:
    model = Drawing
    fields = ['id', 'title', 'image', 'data', 'is_public', 'created_at', 'updated_at', 'user', 'user_id', 'mode'] 