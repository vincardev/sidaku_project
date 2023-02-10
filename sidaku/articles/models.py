from enum import unique
from django.db import models

from django.utils import timezone
from tinymce.models import HTMLField
from django.contrib.auth import get_user_model
from autoslug import AutoSlugField

from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField
import os


class ArticleSeries(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("ArticleSeries", slugify(self.slug), instance)
        return None

    title       = models.CharField(max_length=200)
    subtitle    = models.CharField(max_length=200, default="", blank=True) 
    slug        =  AutoSlugField(populate_from='title', editable=True, unique=True, blank=True, null=True)

#  models.SlugField("Series slug", null=False, blank=False, unique=True)
    published   = models.DateTimeField("Date published", default=timezone.now)
    author      = models.ForeignKey(get_user_model(), default=1, on_delete=models.SET_DEFAULT)
    image       = models.ImageField(default='default/no_image.jpg', upload_to=image_upload_to ,max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Series"
        ordering = ['-published']

class Article(models.Model):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("ArticleSeries", slugify(self.series.slug), slugify(self.article_slug), instance)
        return None

    title           = models.CharField(max_length=200)
    subtitle        = models.CharField(max_length=200, default="", blank=True)
    article_slug    =  AutoSlugField(populate_from='title', editable=True, unique=True, blank=True, null=True)
    # article_slug    = models.SlugField("Article slug", null=False, blank=False, unique=True)
    content         = RichTextUploadingField(blank=True, default="")
    notes           = RichTextUploadingField(blank=True, default="")
    published       = models.DateTimeField("Date published", default=timezone.now)
    modified        = models.DateTimeField("Date modified", default=timezone.now)
    series          = models.ForeignKey(ArticleSeries, default="", verbose_name="Series", on_delete=models.SET_DEFAULT)
    author          = models.ForeignKey(get_user_model(), default=1, on_delete=models.SET_DEFAULT)
    image           = models.ImageField(default='default/no_image.jpg', upload_to=image_upload_to ,max_length=255)
    inheadline      = models.BooleanField(default=False)
    ineducate       = models.BooleanField(default=False)
    ingallery       = models.BooleanField(default=False)


    # created_by      = models.CharField(max_length=25,blank=True, null=True)
    # created_date    = models.DateTimeField(auto_now_add=True)
    # modified_by     = models.CharField(max_length=25,blank=True, null=True)
    # modified_date   = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    @property
    def slug(self):
        return self.series.slug + "/" + self.article_slug

    class Meta:
        verbose_name_plural = "Article"
        ordering = ['-published']