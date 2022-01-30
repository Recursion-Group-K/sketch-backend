from .models import User
from .serializer import UserSerializer
from rest_framework import generics, permissions
# from rest_framework.decorators import action
# from rest_framework.response import Response
from user.permission import UserObjPersmission

# Create your views here.
class UserList(generics.ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
  filter_fields = ('is_superuser', 'is_active')

  # def highlight(self, request, *args, **kwargs):
  #   return Response(request.user)

  def perform_create(self, serializer):
    data = serializer.data
    return User.objects.create_user(**data)

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permissions_classes = [UserObjPersmission]

