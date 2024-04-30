"""
URL configuration for codereviewtrinh project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from posts.views import SignUpView, PostListView, PostCreateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")), #this adds all the built in django logins to the project
    path("signup/", SignUpView.as_view(), name="signup"), #this creates a view out of the form
    path('posts', PostListView.as_view(), name='posts'), #this is supposed to create a view out of this form, but then didn't work out...
    path("post/new/", PostCreateView.as_view(), name="postnew"), 
]
