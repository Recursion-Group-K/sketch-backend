from drawing.permission import IsOwnerOrReadOnly
from .models import Drawing
from .serializer import DrawingSerializer
from rest_framework import generics, permissions
from drawing.permission import IsOwnerOrReadOnly

# Create your views here.
class DrawingList(generics.ListCreateAPIView):
  queryset = Drawing.objects.all()
  serializer_class = DrawingSerializer
  permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
  filter_fields = ('user', 'mode')

  def perform_create(self, serializer):
    # data = serializer.data
    return serializer.save(user=self.request.user)

class DrawingRetrieveUpdate(generics.RetrieveUpdateAPIView):
  queryset = Drawing.objects.all()
  serializer_class = DrawingSerializer
  permissions_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

