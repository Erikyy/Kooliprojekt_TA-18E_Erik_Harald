from django.db import models
from django.contrib.auth.models import User


def prof_dir(instance, filename):
    return "%s/%s" % (instance.user, filename)


class PostManager(models.Manager):
    def private_posts(self, *args, **kwargs):
        user = kwargs.pop('user')
        return super(PostManager, self).filter(user=user)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_img = models.FileField(upload_to=prof_dir)
    title = models.CharField(max_length=50)

    objects = PostManager()

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to=prof_dir, default='default.jpg')
    post = models.ManyToManyField(Post)

    def __str__(self):
        return self.user.username
