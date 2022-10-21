from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    """This is the user profile model"""

    image = models.ImageField(default="avatar.png", null=True, blank=True)
    city = models.CharField(max_length=84, null=True, default="")
    mobile = models.CharField(max_length=84, null=True, default="")
    username = models.CharField(max_length=83, null=False, primary_key=True)

    def __str__(self):

        return self.username


class Reviews(models.Model):

    """This is the reviews model"""

    business_id = models.CharField(max_length=84, null=False)
    username = models.CharField(max_length=84, null=False)
    image_url = models.CharField(max_length=100, null=True)
    review_text = models.TextField(null=False)
    timestamp = models.CharField(max_length=200, null=False)

    def __str__(self):

        return f"{self.business_id} {self.username}"
