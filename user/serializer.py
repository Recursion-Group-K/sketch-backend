from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):

  def validate_password(self, value: str) -> str:
        return make_password(value)

  class Meta:
    model = User
    fields = ['id', 'username', 'email', 'is_active', 'is_superuser', 'password'] 
    extra_kwargs = {'password': {'write_only': True}}