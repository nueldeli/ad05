import string
import random
from django.utils.text import slugify 

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for i in range(size))

def unique_slug_generator(instance, new_slug = None):
	if new_slug is not None:
		slug = new_slug
	else:
		slug = slugify(instance.title)

	a = instance.__class__
	b_exists = a.objects.filter(slug = slug).exists()

	if b_exists:
		new_slug = "{slug}-{randstr}".format(slug=slug, randstr=random_string_generator(size=4))

		return unique_slug_generator(instance, new_slug=new_slug)
	return slug