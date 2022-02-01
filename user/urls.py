from user.views import UserViewSet
from user import views
from django.urls import path

user_list = UserViewSet.as_view({
  'get': 'list',
  'post': 'create'
})


urlpatterns = [
  path('', user_list, name='user_list'),
  path('<int:pk>/', views.UserRetrieveUpdateDestroy.as_view()),
]