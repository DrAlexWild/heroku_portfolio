"""config URL Configuration

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
    2. Add a URL to urlpatterns:  path('blog.html/', include('blog.html.urls'))
"""
import django

from django.contrib import admin
from django.urls import path

#part 6 imports
from django.shortcuts import render


#my imports
from portfolio import views
#para imagens
from django.conf import settings
from django.conf.urls.static import static

app_name = "portfolio"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page_view, name='home'),
    path('about_me', views.about_me_page_view, name='about_me'),
    path('blog', views.blog_page_view, name='blog'),
    path('edita/<int:blog_post_id>', views.edita_blog_post_view, name='edita'),
    path('apaga/<int:blog_post_id>', views.apaga_blog_post_view, name='apaga'),
    path('nova/', views.nova_blog_post_view, name='nova'),
    path('web_programming/', views.web_programming_view, name='web_programming'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('projects', views.projects_view, name='projects'),
]

#para imagens
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)