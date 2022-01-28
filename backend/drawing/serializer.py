from rest_framework import serializers
from .models import Drawing

class DrawingSerializer(serializers.ModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.username')
  class Meta:
    model = Drawing
    fields = ['id', 'title', 'image', 'data', 'is_public', 'created_at', 'updated_at', 'user', 'mode'] 