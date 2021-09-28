from django.contrib import admin
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
	list_display = ('date_input', 'link_name', 'link_link')

admin.site.register(Link, LinkAdmin)