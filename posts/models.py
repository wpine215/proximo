from django.contrib.gis.db import models

class Post(models.Model):
    # If author (User) is deleted, set to NULL
    id = models.AutoField(primary_key = True)
    content = models.CharField(max_length = 140)
    timestamp = models.DateTimeField(auto_now_add = True)
    location = models.PointField(null = False, blank = False)
    city = models.CharField(max_length = 30)
    author = models.ForeignKey('User', null = True, on_delete = models.SET_NULL)
    likes = models.PositiveIntegerField(default = 0)
    reports = models.PositiveIntegerField(default = 0)
    views = models.PositiveIntegerField(default = 0)

class Comment(models.Model):
    # If parent post or comment is deleted, cascade (delete) self as well
    # If author (User) is deleted, set to NULL
    id = models.AutoField(primary_key = True)
    parent = models.ForeignKey('Post', on_delete = models.CASCADE)
    parent_comment = models.ForeignKey('self', null = True, on_delete = models.CASCADE)
    content = models.CharField(max_length = 140)
    timestamp = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey('User', null = True, on_delete = models.SET_NULL)
    likes = models.PositiveIntegerField(default = 0)
    reports = models.PositiveIntegerField(default = 0)