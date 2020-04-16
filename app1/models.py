from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=150)
    post = models.TextField(max_length=500)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='post')

    def __str__(self):
        return self.title


class Product(models.Model):
    pno = models.IntegerField()