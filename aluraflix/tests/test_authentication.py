from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):
    
    def setUp(self):
        self.list_url = reverse('programas-list')
        self.user = User.objects.create_user('c3po', password='123456')
        
    def test_authentication_user(self):
        """test verify credencials correcty authenticate"""
        user = authenticate(username = 'c3po', password = '123456')
        self.assertTrue((user is not None) and user.is_authenticated)    
        
    def test_not_authorized_requisition(self):
        """Test verifi no authenticated get"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_authenticate_incorrecty_username(self):
        """test verify credencials incorrecty authenticate"""
        user = authenticate(username = 'c3pp', password = '123456')
        self.assertFalse((user is not None) and user.is_authenticated) 
        
    def test_authenticate_incorrecty_password(self):
        """test verify credencials incorrecty authenticate"""
        user = authenticate(username = 'c3pp', password = '123455')
        self.assertFalse((user is not None) and user.is_authenticated)
        
    def test_get_authenticated_user(self):
        """Test GET with autehnticated user""" 
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
                      