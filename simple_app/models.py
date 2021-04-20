from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=260)
    author = models.CharField(max_length=260)
    text = models.TextField()
    create_date = models.TimeField(default = timezone.now())
    posted_date = models.TimeField(blank = False, null = True)
    favourite = models.ManyToManyField(User, related_name='favourite', blank = True)
    likes = models.ManyToManyField(User,related_name='likes', blank = True)
    image = models.ImageField(upload_to='images/', blank=True)

    def publish_post(self):
        self.posted_date = timezone.now()
        self.save()

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url():
        return reverse('post_detail', kwargs = {'pk':self.pk})


class Comment(models.Model):

    post = models.ForeignKey('simple_app.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=260)
    text = models.TextField(max_length=260)
    posted_date = models.TimeField(default = timezone.now())

    def get_absolute_url():
        return reverse('post_list')

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/', blank=True)
