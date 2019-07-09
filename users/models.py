from django.contrib.gis.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key = True)
    phone = PhoneNumberField()
    history = models.MultiPointField(blank = True)
    # Accrue user statistics
    num_posts = models.PositiveIntegerField(default = 0)
    num_comments = models.PositiveIntegerField(default = 0)
    num_reports = models.PositiveIntegerField(default = 0)
    num_violations = models.PositiveIntegerField(default = 0)
    # 0 = no ban, 1 = shadowban, 2 = visible mute, 3 = visible global ban
    ban_level = models.IntegerField(default = 0, validators=[MinValueValidator(0), MaxValueValidator(3)])
