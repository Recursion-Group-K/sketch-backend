from rest_framework import serializers
from .models import Drawing
from user.models import User
from user.serializer import UserSerializer

class DrawingSerializer(serializers.ModelSerializer):
  user = UserSerializer(read_only=True)
  user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True) #write_only=Trueを指定する事によってGET時にこのフィールドを出さないようにする
  class Meta:
    model = Drawing
    fields = ['id', 'title', 'image', 'data', 'is_public', 'created_at', 'updated_at', 'user', 'user_id', 'mode'] 

  def create(self, validated_data):
    validated_data['user'] = validated_data.get('user_id', None)

    if validated_data['user'] is None:
      raise serializers.ValidationError('user not found.')
    
    # delete object
    del validated_data['user_id']
    
    return Drawing.objects.create(**validated_data)