from django.urls import path
from .views import PageIndexView

urlpatterns = [
	path('', PageIndexView.as_view(), name='page_index')
]