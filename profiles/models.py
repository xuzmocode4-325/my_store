from django.db import models
from django.views.generic.base import TemplateView 

# Create your models here.

class UserProfile(models.Model):
    image = models.ImageField(upload_to="images")
