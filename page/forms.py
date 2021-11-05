from django import forms
from .models import Post
from django.utils.translation import gettext_lazy as _

class AddPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('author', 'title', 'slug', 'content')

		widgets = {
			'author':forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'writer', 'type':'hidden'}),
			'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Post title'}),
			'slug':forms.TextInput(attrs={'class':'form-control', 'placeholder':'OK to leave empty'}),
			'content':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Start writing'})
		}

		labels = {
			'author':_(''),
			'title':_(''),
			'slug':_(''),
			'content':_('')
		}