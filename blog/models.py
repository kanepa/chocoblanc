from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)

    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title