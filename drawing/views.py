from .models import Drawing
from .serializer import DrawingSerializer
from rest_framework import generics, permissions

# Create your views here.
class DrawingList(generics.ListAPIView):
  queryset = Drawing.objects.all()
  serializer_class = DrawingSerializer
  permissions_classes = [permissions.IsAuthenticated]

class DrawingCreate(generics.CreateAPIView):
  queryset = Drawing.objects.all()
  serializer_class = DrawingSerializer
  permissions_class = [permissions.IsAdminUser]

class DrawingRetrieveUpdate(generics.RetrieveUpdateAPIView):
  queryset = Drawing.objects.all()
  serializer_class = DrawingSerializer
  permissions_classes = [permissions.IsAuthenticated]

