# Generated by Django 4.1 on 2022-10-26 19:00

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_article_article_slug_alter_articleseries_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=True, null=True, populate_from='title', unique=True),
        ),
        migrations.AlterField(
            model_name='articleseries',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=True, null=True, populate_from='title', unique=True),
        ),
    ]
