from django.shortcuts import render
from django.http import HttpResponse
from animalscience.webapp.models import ProjectsData
from animalscience.webapp.models import researchdata, author_entity
from .forms import PostForm
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
	# articles_title_list = author_entity.objects.values_list('last_name').filter(last_name="a")
	articles_title_list = researchdata.objects.order_by('article_title')
	context = {'articles_title_list':articles_title_list}
	return render(request, 'articles.html', context)

def contact_us(request):
	return render(request, 'contact_us.html')

def peoples_amanda(request):
	return render(request, 'peoples_amanda.html')

def peoples_emily(request):
	return render(request, 'peoples_emily.html')

def peoples_rachel(request):
	return render(request, 'peoples_rachel.html')
