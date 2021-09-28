from django.shortcuts import render
from .models import Link
from django.views.generic import ListView

# Create your views here.
class PageIndexView(ListView):
	model = Link
	template_name = 'page/page_index.html'

