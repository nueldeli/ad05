from django.db import models
from django.urls import reverse
from .utils import unique_slug_generator
from django.db.models.signals import pre_save 
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):
	date_written = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
	content = RichTextUploadingField(blank=True)

	class Meta:
		ordering = ['-date_written']

	def __str__(self):
		return self.title + ' | ' + str(self.author)

	def get_absolute_url(self):
		return reverse('post_detail', kwargs={'slug':self.slug})

#This function runs when a signal calls it (For slugify-ing the slug)
def slug_generator(sender, instance, *args, **kwargs):
		if not instance.slug:
			instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Post)