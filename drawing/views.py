from drawing.permission import IsOwnerOrReadOnly
from .models import Drawing
from .serializer import DrawingSerializer
from rest_framework import generics, permissions
from drawing.permission import IsOwnerOrReadOnly

# Create your views here.
class DrawingList(generics.ListAPIView):
  queryset = Drawing.objects.all()
  serializer_class = DrawingSerializer
  permissions_classes = [permissions.IsAuthenticated]
  filter_fields = ('user', 'mode')

class DrawingCreate(generics.CreateAPIView):
  queryset = Drawing.objects.all()
  serializer_class = DrawingSerializer
  permissions_class = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class DrawingRetrieveUpdate(generics.RetrieveUpdateAPIView):
  queryset = Drawing.objects.all()
  serializer_class = DrawingSerializer
  permissions_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

