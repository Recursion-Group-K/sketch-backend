from django.urls import path
from user import views

urlpatterns = [
  path('', views.UserList.as_view()),
  path('<int:pk>/', views.UserRetrieveUpdate.as_view())
]