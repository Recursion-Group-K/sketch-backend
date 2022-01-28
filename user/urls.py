from django.urls import path
from user import views

urlpatterns = [
  path('user/', views.UserList.as_view()),
  path('create-user/', views.UserCreate.as_view()),
  path('users/<int:pk>/', views.UserRetrieveUpdate.as_view())
]