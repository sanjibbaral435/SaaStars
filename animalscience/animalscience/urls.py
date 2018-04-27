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
#from django.urls import path
from animalscience.webapp import views
from django.conf.urls import url, include

urlpatterns = [
    #path('admin/', admin.site.urls),
    #url(r'^admin/$',admin.site.urls),
]

#Use include() to add paths from the webapp application 
#from django.urls import include

urlpatterns += [
    #path('webapp/', include('animalscience.webapp.urls')),
]

#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
#urlpatterns += [
#    path('', RedirectView.as_view(url='/webapp/')),
#]

urlpatterns = [
    #path('', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^research/', views.research, name='research'),
    url(r'^peoples/', views.peoples, name='peoples'),
    url(r'^courses/', views.courses, name='courses'),
    url(r'^articles/', views.articles, name='articles'),
    url(r'^projects/', views.projects, name='projects'),
    url(r'^get_involved/', views.get_involved, name='get_involved'),
    url(r'^contact_us/', views.contact_us, name='contact_us'),
    url(r'^peoples_amanda/', views.peoples_amanda, name='peoples_amanda'),
    url(r'^peoples_rachel/', views.peoples_rachel, name='peoples_rachel'),
    url(r'^peoples_emily/', views.peoples_emily, name='peoples_emily'),
    url(r'^admin/',admin.site.urls, name ='admin'),
]

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)