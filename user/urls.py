from user.views import UserViewSet
from user import views
from django.urls import path
from rest_framework import renderers

user_list = UserViewSet.as_view({
  'get': 'list',
  'post': 'create'
})
user_highlight = UserViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])


urlpatterns = [
  path('users/', user_list, name='user_list'),
  path('users/<int:pk>/', views.UserRetrieveUpdateDestroy.as_view(), name='user_detail'),
  path('current_user/', user_highlight, name='user_highlight'),
]