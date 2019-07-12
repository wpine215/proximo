from django.contrib.gis.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    phone = PhoneNumberField()
    history = models.MultiPointField(blank = True)
    # Accrue user statistics
    num_posts = models.PositiveIntegerField(default = 0)
    num_comments = models.PositiveIntegerField(default = 0)
    num_reports = models.PositiveIntegerField(default = 0)
    num_violations = models.PositiveIntegerField(default = 0)
    # Bans will be dealt with using Django built-in support for groups
