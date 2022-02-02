from django.http import JsonResponse
from .models import User
from .serializer import UserSerializer
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import action
from user.permission import UserObjPersmission



# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
  filter_fields = ('is_superuser', 'is_active')

  @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
  def highlight(self, request, *args, **kwargs):
    serializer = UserSerializer(request.user)
    return JsonResponse(serializer.data)

  def perform_create(self, serializer):
    data = serializer.data
    return User.objects.create_user(**data)

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permissions_classes = [UserObjPersmission]

