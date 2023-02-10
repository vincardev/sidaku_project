# Generated by Django 4.1 on 2022-10-26 18:47

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_slug',
            field=autoslug.fields.AutoSlugField(editable=True, populate_from='title', unique=True),
        ),
        migrations.AlterField(
            model_name='articleseries',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=True, populate_from='title', unique=True),
        ),
    ]
