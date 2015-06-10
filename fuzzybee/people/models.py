from django.db import models
from django.contrib.auth.models import User
from utils.constant import GENDER

class People(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=24, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER)
    avatar = models.ImageField(upload_to='avatar')
    reserved = models.CharField(max_length=140)

    def avatar_url(self):
        """
        Returns the URL of the image associated with this Object.
        If an image hasn't been uploaded yet, it returns a stock image

        :returns: str -- the image url

        """
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        else:
            return 'default'
