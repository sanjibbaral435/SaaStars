"""animalscience URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from animalscience.webapp import views
from django.conf.urls import url, include

urlpatterns = [
    #path('admin/', admin.site.urls),
    #url(r'^admin/$',admin.site.urls),
]

#Use include() to add paths from the webapp application 
from django.urls import include

urlpatterns += [
    path('webapp/', include('animalscience.webapp.urls')),
]

#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
#urlpatterns += [
#    path('', RedirectView.as_view(url='/webapp/')),
#]

urlpatterns = [
    #path('', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^view_phages/$', views.view_phages, name='view_phages'),
    url(r'^search_phage/$', views.search_phage, name='search_phage'),
    url(r'^about_us/', views.about_us, name='about_us'),
    url(r'^peoples/', views.peoples, name='peoples'),
    url(r'^projects/', views.projects, name='projects'),
    url(r'^articles/', views.articles, name='articles'),
    url(r'^contact_us/', views.contact_us, name='contact_us'),
    url(r'^search_phage/$', views.search_phage, name='search_phage'),
    url(r'^admin/',admin.site.urls),
]

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)