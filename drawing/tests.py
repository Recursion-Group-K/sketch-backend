from multiprocessing.dummy.connection import Client

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Drawing

# Create your tests here.
# class TestDrawings(APITestCase):
#   # def get_token(self):
#   #   url = reverse('token_obtain_pair')
#   #   drawing = Drawing.objects.create()
#   #   response = self.client.post(url, drawing, format='json')
#   #   token = response.data['access']
#   #   print("Token: " + token)
#   #   return token

#   # def test_api_drawings(self):

#   #   url = '/api/drawings/'



#   #   # self.client.credentials(HTTP_AUTHORIZATION='Token ' + 'faketoken')
#   #   # response = self.client.get(url, data={'format': 'json'})
#   #   # self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
#   #   token = self.get_token()
#   #   self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
#   #   response = self.client.get(url, data={'format': 'json'})
#   #   response_detail = self.client.get(url+'1', data={'format': 'json'})

#   #   self.assertEqual(response.status_code, status.HTTP_200_OK)
#   #   self.assertEqual(response_detail.status_code, status.HTTP_200_OK)

#   def test_drawings(self):
#     url = reverse('token_obtain_pair')
#     drawing = Drawing.objects.create()
#     response = self.client.post(url, drawing, format='json')
#     token = response.data['access']
#     print("Token: " + token)