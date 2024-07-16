from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    profile_photo = models.ImageField(upload_to="user/photos/", blank=True, null=True)
