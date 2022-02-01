from user.views import UserViewSet
from rest_framework import renderers
from user import views
from django.urls import path

user_list = UserViewSet.as_view({
  'get': 'list',
  'post': 'create'
})

user_highlight = UserViewSet.as_view({
  'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

urlpatterns = [
  path('', user_list, name='user_list'),
  path('<int:pk>/', views.UserRetrieveUpdateDestroy.as_view()),
  path('', user_highlight, name='user_highlight'),
]