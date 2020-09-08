from django.db import models
from django.contrib.auth.models import User


def prof_dir(instance, filename):
    return "%s/%s" %(instance.user, filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to=prof_dir, blank=True)
    
    #Gallery stuff
    post_img = models.ImageField(upload_to=prof_dir, null=True)
    title = models.CharField(max_length=50, null=True)
    

    def __str__(self):
        return self.user.username



    

    
    
    


    
