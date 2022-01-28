from django.urls import path
from drawing import views

urlpatterns = [
  path('drawing/', views.DrawingList.as_view()),
  path('create-drawing/', views.DrawingCreate.as_view()),
  path('drawing/<int:pk>/', views.DrawingRetrieveUpdate.as_view())
]