from django.test import TestCase, Client

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from animalscience.webapp.models import author_entity
from animalscience.webapp.models import key_entity
from animalscience.webapp.models import article_entity

from animalscience.webapp.forms import PostForm

import animalscience.webapp.views
from django.urls import reverse
import sys

from urllib.request import urlopen
import json

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



class PostFormTest(TestCase):
    @classmethod
    def test_renew_title_label(self):
        form = PostForm()  
        resp = form.fields['title'].label 
        self.assertTrue(resp is 'Article Title', True)

    def test_renew_publication_label(self):
        form = PostForm()
        resp = form.fields['year'].label 
        self.assertTrue(resp == 'Year of Publication', True)

    def test_renew_author_label(self):
        form = PostForm()
        resp = form.fields['author'].label 
        self.assertTrue(str(resp) == 'Author Name', True)

    def test_renew_keyword_label(self):
        form = PostForm()
        resp = form.fields['keyword'].label
        self.assertTrue(resp == 'Keywords', True)


#py.test -x -s MYPACKAGE --cov-report html --cov MYPACKAGE

class ViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Create 13 authors for pagination tests
        number_of_articles = 13
        for article_num in range(number_of_articles):
            article_entity.objects.create(article_title = "burrow %s" % article_num, link="https://burrows.pdf %s" % article_num, article_year ="1992")
            # article_entity.objects.create(first_name='Christian %s' % author_num, last_name = 'Surname %s' % author_num,)
           
    def test_view_url_exists_at_desired_location(self): 
        resp = self.client.get('/articles/') 
        self.assertEqual(resp.status_code, 200)  
           
    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('articles'))
        self.assertEqual(resp.status_code, 200)
        
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('articles'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'articles.html')

    def test_lists_all_articles(self):
        resp = self.client.get(reverse('articles'))
        print ("dfjkajkjfdljfaljf", resp.context)
        sys.stdout.flush()
        self.assertEqual(resp.status_code, 200)
        self.assertTrue( len(resp.context['articles_title_list']) == 13)
        
    def test_page_rachel(self):
        resp = self.client.get('/peoples_rachel/') 
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'peoples_rachel.html')
    
    def test_page_amanda(self):
        resp = self.client.get('/peoples_amanda/') 
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'peoples_amanda.html')
    
    def test_page_emily(self):
        resp = self.client.get('/peoples_emily/') 
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'peoples_emily.html')
    
    def test_page_awdjt(self):
        resp = self.client.get('/awjt/') 
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'awjt.html')

    # def test_page_index(self):
    #     resp = self.client.get('/$') 
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertTemplateUsed(resp, 'index.html')
    
    def test_page_research(self):
        resp = self.client.get('/research/') 
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'research.html')
        
    def test_page_courses(self):
        resp = self.client.get('/courses/') 
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'courses.html')

    def test_page_get_involved(self):
        resp = self.client.get('/get_involved/') 
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'get_involved.html')
        
    def test_page_projects(self):
        resp = self.client.get('/projects/') 
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'projects.html')
        
    def test_page_peoples(self):
        resp = self.client.get('/peoples/') 
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'peoples.html')
        
    def test_page_contact_us(self):
        resp = self.client.get('/contact_us/') 
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'contact_us.html')
        

    # def test_add_phage_req(self):
    #     data = {"phage_lab": "Lab-A", "flag":1}
    #     #self.client.login(username = "test_user", password= 'pass@123')
    #     response = self.client.post('/articles/', data, follow=True)
    #     approvePhage = response.json()['approvePhage']
    #     approveCPTid = response.json()['approveCPTid']
    #     self.assertEqual(approvePhage,1)
    #     self.assertEqual(approveCPTid,1)
        
    def test_addAccount(self):
        #article_entity.objects.create(article_title = "burrow", link="https://burrows.pdf", article_year ="1992")
        #print ("\n My sample testcase \n")
        response = self.client.post('/contact_us/',{'name':'pussycat dolls','email':"myhumps@gmail.com",'message':"myhumps_lovely little lumps","email_about":"kuch bhiii bc"}, follow = True)
        print (response)
        #print("---------------------------------------",response.read().decode('utf-8'),"++++++++++++++++++++++++++++++++++++++++++")
        #string = response[1])
        print( "========*****=========")
        #print(response.content)
        #json_obj = json.loads(string)
        self.assertEqual(response.status_code, 200) 