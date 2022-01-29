from .models import User
from .serializer import UserSerializer
from rest_framework import generics, permissions

# Create your views here.
class UserList(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permissions_classes = [permissions.IsAuthenticated]
  filter_fields = ('is_superuser', 'is_active')

class UserCreate(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permissions_class = [permissions.IsAdminUser]

  def perform_create(self, serializer):
    data = serializer.data
    return User.objects.create_user(**data)

class UserRetrieveUpdate(generics.RetrieveUpdateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permissions_classes = [permissions.IsAuthenticated]

