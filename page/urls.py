from django.urls import path
from .views import PostIndexView, PostAddView

urlpatterns = [
	path('post_index/', PostIndexView.as_view(), name='post_index'),
	path('post_add/', PostAddView.as_view(), name='post_add'),
]