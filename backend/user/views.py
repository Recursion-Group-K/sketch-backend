from .models import User
from .serializer import UserSerializer
from rest_framework import generics, permissions

# Create your views here.
class UserList(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permissions_classes = [permissions.IsAuthenticated]

class UserCreate(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permissions_class = [permissions.IsAdminUser]

  # def perform_create(self, serializer):
  #   data = serializer.data
  #   password = data.pop('password', 'something')

class UserRetrieveUpdate(generics.RetrieveUpdateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permissions_classes = [permissions.IsAuthenticated]

