from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.


class MyUser(AbstractUser):

    date_of_birth = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
