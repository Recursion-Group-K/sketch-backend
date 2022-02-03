from rest_framework.test import APITestCase
from ..models import User

class TestModel(APITestCase):

  def test_create_user(self):
    user = User.objects.create_user('test', 'test@gmail.com', 'test123')

    self.assertIsInstance(user, User)
    self.assertFalse(user.is_staff)
    self.assertFalse(user.is_superuser)
    self.assertEqual(user.username, "test")
    self.assertEqual(user.email, "test@gmail.com")

  def test_create_super_user(self):
    user = User.objects.create_superuser('test', 'test@gmail.com', 'test123')

    self.assertIsInstance(user, User)
    self.assertTrue(user.is_staff)
    self.assertTrue(user.is_superuser)
    self.assertEqual(user.username, "test")
    self.assertEqual(user.email, "test@gmail.com")
    
  def test_raise_error_in_create_user(self):
    # creating user with no username should raise error 
    self.assertRaises(ValueError, User.objects.create_user, username='', email='test@gmail.com', password='test123')
    # make sure the error message is the one we set 
    with self.assertRaisesMessage(ValueError, 'The given username must be set'):
      User.objects.create_user(username='', email='test@gmail.com', password='test123')
    self.assertRaises(ValueError, User.objects.create_user, username='test', email='', password='test123')
    with self.assertRaisesMessage(ValueError, 'The given email must be set'):
      User.objects.create_user(username='test', email='', password='test123')

  def test_raise_error_in_super_user(self):
    with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
      User.objects.create_superuser(username='test', email='test@gmail.com', password='test123', is_staff=False)

    with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
      User.objects.create_superuser(username='test', email='', password='test123', is_superuser=False)