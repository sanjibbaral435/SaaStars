from django.shortcuts import render
from django.http import HttpResponse
from animalscience.webapp.models import ProjectsData
from animalscience.webapp.models import researchdata, author_entity, article_entity, key_entity
from animalscience.webapp.forms import PostForm
from django.db.models import Value as V
from django.db.models.functions import Concat
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
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
	projects_title_list = ProjectsData.objects.order_by('project_title')
	context = {'projects_title_list':projects_title_list}
	#form = PostForm()
	
	form = PostForm(request.POST)
	if form.is_valid():
	    post = form.save(commit=False)
	    #post.title = request.title
	    #post.text = request.text
	    print(form)
	    #post.save()
	    #return redirect('post_detail', pk=post.pk)
	    
	return render(request, 'projects.html', {'form': form}, context)
	
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
			#articles_title_list.union(articles_years_list)
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

def login(request):
    msg = dict()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        print (form.errors)
        username = request.POST['username']
        password = request.POST['password']
        if form.is_valid():
            msg['form_is_valid'] = True
        else:
            form.add_error('password', 'Please enter a correct username and password. Note that both fields are case-sensitive.')
            msg['form_is_valid'] = False

        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    msg['form_is_valid'] = True
                else:
                    msg['form_is_valid'] = False
    else:
        form = AuthenticationForm()
    context = {'form': form}
    msg['html_form'] = render_to_string('partial_login.html',
                                         context,
                                         request=request
                                         )
    return JsonResponse(msg)