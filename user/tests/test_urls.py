from urllib import response
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import User

# Create your tests here.
class TestTokenAuth(APITestCase):

  def test_api_token_auth(self):
    # 構築
    url = reverse('token_obtain_pair')
    user = User.objects.create_user(username="test", email="test@gmail.com", password="test123")
    # 操作
    user.is_active = False
    user.save()

    response = self.client.post(url, {"email": "test@gmail.com", "password": "test123"}, format='json')
    # 検証
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    # 操作
    user.is_active = True
    user.save()

    response = self.client.post(url, {"username": "test", "password": "test123"}, format='json')
    # 検証
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertTrue('access' in response.data)

class TestUserEndPoints(APITestCase):

  def get_token(self):
    url = reverse('token_obtain_pair')
    user = User.objects.create_user(username="test", email="test@gmail.com", password="test123")
    user.is_active = True
    user.save()
    response = self.client.post(url, {"username": "test", "password": "test123"}, format='json')
    token = response.data['access']
    print("Bearer " + token)
    return token

  # def test_api_current_user(self):

  #   url = '/api/current_user/'
  #   self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + 'faketoken')
  #   response = self.client.get(url, data={'format': 'json'})
  #   self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
  #   token = self.get_token()
  #   self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
  #   response = self.client.get(url, data={'format': 'json'})
  #   self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_api_user_list(self):

    url = '/api/users/'
    self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + 'faketoken')
    response = self.client.get(url, data={'format': 'json'})
    self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    token = self.get_token()
    self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
    response = self.client.get(url, data={'format': 'json'})
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  # def test_api_user_by_id(self):
  #   url = '/api/users/1/'
  #   user = User.objects.create_user(username="test", email="test@gmail.com", password="test123")
  #   user.is_active = True
  #   user.save()
  #   response = self.client.get(url, data={'format': 'json'})
  #   self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
  #   print(response.data)



