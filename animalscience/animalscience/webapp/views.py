from django.shortcuts import render
from django.http import HttpResponse
from animalscience.webapp.models import author_entity, article_entity, key_entity
from animalscience.webapp.forms import PostForm
from animalscience.webapp.forms import contact_form
from django.db.models import Value as V
from django.db.models.functions import Concat
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import redirect
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
# Create your views here.

def index(request):
    """
    View function for home page of site.
    """
    return render(request,'index.html')

def research(request):
	return render(request, 'research.html')

def peoples(request):
	return render(request, 'peoples.html')

def courses(request):
	return render(request, 'courses.html')
	
def get_involved(request):
	return render(request, 'get_involved.html')
	
def projects(request):
	return render(request, 'projects.html')	

def articles(request):
	article_page = 'articles.html'
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']
			year = form.cleaned_data['year']
			author = form.cleaned_data['author']
			keyword = form.cleaned_data['keyword']
			print(title, year, author, keyword)
			articles_title_list = article_entity.objects.filter(article_title__icontains=title)
			if year!="":
				articles_title_list = articles_title_list.filter(article_year=year)
			if author!="":
				author_list= author_entity.objects.annotate(name = Concat('first_name',V(' '),'last_name')).filter(name__icontains=author)
				articles_title_list = articles_title_list.filter(authors__in=author_list).distinct()
			if keyword!="":
				keyword_list= key_entity.objects.filter(keyword__icontains=keyword)
				articles_title_list = articles_title_list.filter(keywords__in=keyword_list).distinct()
			# articles_title_list.union(articles_years_list)
			print(articles_title_list)
			context = {'articles_title_list':articles_title_list,'form':form}
			return render(request, article_page, context)
	elif request.method == 'GET':
		form = PostForm();
		articles_title_list = article_entity.objects.order_by('article_title')
		print(articles_title_list)
		context = {'articles_title_list':articles_title_list,'form':form}
		return render(request, article_page,context)
	

def contact_us(request):
	return render(request, 'contact_us.html')

def peoples_amanda(request):
	return render(request, 'peoples_amanda.html')

def peoples_emily(request):
	return render(request, 'peoples_emily.html')

def peoples_rachel(request):
	return render(request, 'peoples_rachel.html')

def awjt(request):
	return render(request, 'awjt.html')

# def login(request):
#     msg = dict()
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         print (form.errors)
#         username = request.POST['username']
#         password = request.POST['password']
#         if form.is_valid():
#             msg['form_is_valid'] = True
#         else:
#             form.add_error('password', 'Please enter a correct username and password. Note that both fields are case-sensitive.')
#             msg['form_is_valid'] = False
#         if username and password:
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     msg['form_is_valid'] = True
#                 else:
#                     msg['form_is_valid'] = False
#     else:
#         form = AuthenticationForm()
#     context = {'form': form}
#     msg['html_form'] = render_to_string('partial_login.html',
#                                          context,
#                                          request=request
#                                          )
#     return JsonResponse(msg)

def contact(request):
    if request.method == 'GET':
        form = contact_form()
    else:
        form = contact_form(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['name']
            contact_email = form.cleaned_data['email']
            contact_message = "Message: " + form.cleaned_data['message']
            subject = form.cleaned_data['email_about']
            
            toaddr = getemail(subject)
            try:
                fromaddr = contact_name + contact_email
                msg = MIMEMultipart()
                msg['From'] = fromaddr
                msg['To'] = ", ".join(toaddr)
                msg['Subject'] = "Message From AWBL Website: " + subject
                body = "Name: " + contact_name + "\n" + "Email: " + contact_email + "\n\n\n" + contact_message
                msg.attach(MIMEText(body, 'plain'))
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login("tamu.awbl", "awbladmin123")
                text = msg.as_string()
                server.sendmail(fromaddr, toaddr, text)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, "contact_us.html", {'form': form})
    return render(request, "contact_us.html", {'form': form})
    
def getemail(subject):
    if subject == 'Undergraduate research' or subject == 'Graduate research' or subject == 'Other':
    	return 'cdaigle@tamu.edu'
    elif subject == 'Animal welfare club':
    	return ['cdaigle@tamu.edu', 'menenses@tamu.edu']
    else:
    	return ['cdaigle@tamu.edu', 'rachelpark@tamu.edu']