# Generated by Django 3.2.6 on 2021-11-02 04:50

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_written', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_written'],
            },
        ),
    ]
