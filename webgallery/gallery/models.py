from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from os import path


def prof_dir(instance, filename):
    return "%s/%s" % (instance.user, filename)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_img = models.ImageField(upload_to=prof_dir)
    title = models.CharField(max_length=50)
    create_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    def file_name(self):
        return path.basename(self.post_img.name)

    def file_extension(self):
        name, extension = path.splitext(self.post_img.name)
        return extension

    def file_size(self):
        return f"{self.post_img.size / 1000000} MB"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to=prof_dir, default='default.jpg', blank=True)

    def __str__(self):
        return self.user.username
