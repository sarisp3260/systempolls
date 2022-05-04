"""systempolls URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from polls import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    #path('create/', views.create, name='create'),
    path('create/', views.create2, name='create'),
    #path('vote/<poll_id>/', views.vote, name='vote'),
    path('vote/<poll_id>/', views.vote2, name='vote'),
    #path('results/<poll_id>/', views.results, name='results'),
    path('results/<poll_id>/', views.results2, name='results'),

]
