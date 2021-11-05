from django.shortcuts import render
from .models import Post
from .forms  import AddPostForm
from django.views.generic import ListView, CreateView

# Create your views here.
class PostIndexView(ListView):
	model = Post
	template_name = 'page/post_index.html'

class PostAddView(CreateView):
	model = Post
	form_class = AddPostForm
	template_name = 'page/post_add.html'

