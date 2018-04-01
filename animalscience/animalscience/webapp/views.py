from django.shortcuts import render
from django.http import HttpResponse
from animalscience.webapp.models import ProjectsData
from animalscience.webapp.models import researchdata
# Create your views here.

def index(request):
    """
    View function for home page of site.
    """
    return render(request,'index.html')


def view_phages(request):

	return render(request,'view_phages.html')

def search_phage(request):
	return render(request,'search_phage.html')

def about_us(request):
	return render(request, 'about_us.html')

def peoples(request):
	return render(request, 'peoples.html')

def projects(request):
	projects_title_list = ProjectsData.objects.order_by('project_title')
	context = {'projects_title_list':projects_title_list}
	return render(request, 'projects.html', context)
	
def articles(request):
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
