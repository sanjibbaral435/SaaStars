from django.test import TestCase, Client


from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model




# Create your tests here.
class SimpleTest(TestCase):
    # def setUp(self):
    #     user = User.objects.create_user('ssss', 'ssss')
    #     user.save()
    #     print(user)
    valid_credentials = {
        'username': "hg",
        'password': 'qwerty1234'}
    invalid_credentials = {
        'username': 'abcde',
        'password': '12345'}

    def create_user(self):
        self.username = "hg"
        self.password = "12345"
        user, created = User.objects.get_or_create(username=self.username)
        print(user, created)
        #user.set_password(self.password)
        user.is_staff = True
        #user.is_superuser = True
        #user.is_active = True
        user.save()
        self.user = user
    
    def get_user(self):
        user, get = User.objects.get_by_natural_key("hg")
        print(user, get)
        self.user = user
        

    # def test_secure_page(self):
    #     #self.setUp()
    #     self.client.login(username='temporary', password='temporary')
    #     response = self.client.get('/login/')
    #     print("+++++++++++", response.status_code)
    #     self.assertNotEqual(response.status_code, 200)
    #     #user = User.objects.get(username='temporary')
    #     #self.assertEqual(response.context['email'], 'temporary@gmail.com')
        
    def test_secure_page1(self):
        user, created = User.objects.get_or_create(username="hg")
        print(user, created)
        user.set_password("qwerty1234")
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        superusers = User.objects.filter(is_superuser=True)
        print(superusers)
        print(get_user_model().objects.filter(username="hg").exists())
        self.client.login(username='hh', password='qwerty1234')
        response = self.client.get('/login/')
        print("+++++++++++", response.status_code)
        self.assertEqual(response.status_code, 200)
        
        
        
    # def test_SetUp(self):
    #     self.client = Client()
    #     my_admin = User(username='user', is_staff=True)
    #     my_admin.set_password('passphrase') # can't set above because of hashing
    #     my_admin.save() # needed to save to temporary test db
    #     response = self.client.get('/login/', follow=True)
    #     loginresponse = self.client.login(username='hg',password='qwerty1234')
    #     self.assertTrue(loginresponse) # should now return "true"
        

    # def setUp(self):
    #     self.credentials = {
    #         'username': 'hg',
    #         'password': 'qwerty1234'}
    #     User.objects.create_user(**self.credentials)
        
    # def test_login(self):
    #     # login
    #     response = self.client.post('/login/', **self.credentials)      
    #     # should be logged in now, fails however
    #     self.assertTrue(response.context['user'].is_active)