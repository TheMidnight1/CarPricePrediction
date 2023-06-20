from django.db import models
from django.contrib.auth.models import AbstractUser


# class User(models.Model):
#     first_name = models.CharField(max_length=250, blank=True)
#     last_name = models.CharField(max_length=250, blank=True)
#     email = models.EmailField(unique=True, blank=True)
#     password = models.CharField(max_length=100, blank=True)
#     address = models.CharField(max_length=250, blank=True)
#     date_joined = models.DateTimeField(auto_now_add=True, blank=True)


class User(AbstractUser):
    pass
