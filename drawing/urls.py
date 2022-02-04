from django.urls import path
from drawing import views

urlpatterns = [
  path('', views.DrawingList.as_view()),
  path('<int:pk>/', views.DrawingRetrieveUpdateDetroy.as_view())
]