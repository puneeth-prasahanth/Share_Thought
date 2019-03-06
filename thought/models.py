from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    topic= models.CharField(max_length=100)
    def __str__(self):
            return u"%s" % (self.topic)


class Comment(models.Model):
    ##topic_id=models.ForeignKey(Topic)
    user=models.ForeignKey(User)
    Publish_date = models.DateField(default=timezone.now)
    text = models.TextField()
    tweet_id = models.BigIntegerField(max_length=None,default=0)

