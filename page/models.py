from django.db import models
from django.urls import reverse 

# Create your models here.
class Link(models.Model):
	date_input = models.DateTimeField(auto_now_add=True)
	link_name = models.CharField(max_length=250)
	link_link = models.TextField()

	class Meta:
		ordering = ['-date_input']

	def __str__(self):
		return str(self.date_input) + ' | ' + self.link_name

	def get_absolute_url(self):
		return reverse('page_index')
