from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.forms import UserCreationForm #built in user creation form
from .models import Post
# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

#these would be a seperate view for posting and viewing, i figured it'd be faster because then i wouldn't have to deal with the html, but...
class PostListView(ListView): 
    model = Post
    template_name = "posts.html"

class PostCreateView(CreateView): 
    model = Post
    template_name = "postnew.html"
    fields = ["author", "body"]