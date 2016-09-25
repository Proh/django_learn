from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=200)
    cat = models.ForeignKey(Category,related_name='articles',null = True)

    def __unicode__(self):
        return self.title
