from django.http import JsonResponse
from .models import User
from .serializer import UserSerializer
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from user.permission import UserObjPersmission



# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
  filter_fields = ('is_superuser', 'is_active')

  @action(detail=True)
  def current_user(self, request, *args, **kwargs):
    serializer = UserSerializer(request.user)
    return JsonResponse(serializer.data)

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permissions_classes = [UserObjPersmission]
