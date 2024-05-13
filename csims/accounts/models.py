from django.db import models
from django.contrib import auth
from django.utils import timezone

# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)

# Extend User model to include profile pictures
class UserProfileInfo(models.Model):
   user = models.OneToOneField(auth.models.User, on_delete=models.CASCADE)
   profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics')

   def __str__(self):
      return "{} Profile".format(self.user.username)