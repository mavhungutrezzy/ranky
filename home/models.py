from django.db import models
from django.contrib.auth.models import User


class FoodPlace(models.Model):
    business_id = models.CharField(max_length=100)
    business_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    inspection_type = models.CharField(max_length=100)
    inspection_score = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    risk_category = models.CharField(max_length=100)
    violation_description = models.TextField()

    def __str__(self):
        return self.business_name


class Comment(models.Model):
    foodplace = models.ForeignKey(FoodPlace, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
