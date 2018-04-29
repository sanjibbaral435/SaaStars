from django.test import TestCase, Client

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from animalscience.webapp.models import author_entity
from animalscience.webapp.models import key_entity
from animalscience.webapp.models import article_entity

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
        self.client.login(username='hg', password='qwerty1234')
        response = self.client.get('/admin/')
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







class AuthorModelTest(TestCase):
    author_id = ''
    
    @classmethod
    def setUpTestData(self):
        #Set up non-modified objects used by all test methods
        author_entity.objects.create(first_name='John', last_name='Doe')
        self.author_id = author_entity.objects.get(first_name='John').author_id

    def test_first_name_label(self):
        author = author_entity.objects.get(author_id = self.author_id)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'first name')

    def test_last_name_label(self):
        author = author_entity.objects.get(author_id=self.author_id)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label,'last name')

    def test_first_name_max_length(self):
        author = author_entity.objects.get(author_id=self.author_id)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        author = author_entity.objects.get(author_id=self.author_id)
        expected_object_name = '%s, %s' % (author.last_name, author.first_name)
        self.assertEquals(expected_object_name, str(author))



class KeyModelTest(TestCase):
    key_id = ''
    
    @classmethod
    def setUpTestData(self):
        #Set up non-modified objects used by all test methods
        key_entity.objects.create(keyword='animal')
        self.key_id = key_entity.objects.get(keyword='animal').key_id

    def test_keyword_label(self):
        key = key_entity.objects.get(key_id = self.key_id)
        field_label = key._meta.get_field('keyword').verbose_name
        self.assertEquals(field_label,'keyword')

    def test_keyword_max_length(self):
        key = key_entity.objects.get(key_id=self.key_id)
        max_length = key._meta.get_field('keyword').max_length
        self.assertEquals(max_length, 100)

    def test_keyword_name(self):
        key = key_entity.objects.get(key_id=self.key_id)
        expected_object_name = '%s' % (key.keyword)
        self.assertEquals(expected_object_name, str(key))
        
        
class ArticleModelTest(TestCase):
    article_id = ''
    
    @classmethod
    def setUpTestData(self):
        #Set up non-modified objects used by all test methods
        article = article_entity.objects.create(article_title = "burrow", link="https://burrows.pdf", article_year ="1992")
        article.save()
        self.article_id = article_entity.objects.get(article_title="burrow").article_id

    def test_keywords_label(self):
        article = article_entity.objects.get(article_id = self.article_id)
        field_label = article._meta.get_field('keywords').verbose_name
        self.assertEquals(field_label,'keywords')
    
    def test_articleTitle_label(self):
        article = article_entity.objects.get(article_id = self.article_id)
        field_label = article._meta.get_field('article_title').verbose_name
        self.assertEquals(field_label,'article title')
    
    def test_articleYear_label(self):
        article = article_entity.objects.get(article_id = self.article_id)
        field_label = article._meta.get_field('article_year').verbose_name
        self.assertEquals(field_label,'article year')
    
    def test_link_label(self):
        article = article_entity.objects.get(article_id = self.article_id)
        field_label = article._meta.get_field('link').verbose_name
        self.assertEquals(field_label,'link')
    
    def test_authors_label(self):
        article = article_entity.objects.get(article_id = self.article_id)
        field_label = article._meta.get_field('authors').verbose_name
        self.assertEquals(field_label,'authors')
    
    def test_link_max_length(self):
        article = article_entity.objects.get(article_id=self.article_id)
        max_length = article._meta.get_field('link').max_length
        self.assertEquals(max_length, 200)
        
    def test_articleTitle_max_length(self):
        article = article_entity.objects.get(article_id=self.article_id)
        max_length = article._meta.get_field('article_title').max_length
        self.assertEquals(max_length, 200)
        
    def test_articleYear_max_length(self):
        article = article_entity.objects.get(article_id=self.article_id)
        max_length = article._meta.get_field('article_year').max_length
        self.assertEquals(max_length, 4)

    def test_article_name(self):
        article = article_entity.objects.get(article_id=self.article_id)
        expected_object_name = '%s' % (article.article_title)
        self.assertEquals(expected_object_name, str(article))