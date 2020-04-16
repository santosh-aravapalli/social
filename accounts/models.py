from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):

    ch = [
        ('Male','MALE'),
        ("Female",'FEMALE')
    ]

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    gender = models.CharField(choices=ch,max_length=10)
    age = models.IntegerField()
    date_of_birth = models.DateField()

    def __str__(self):
        return self.user.username+'profile'



