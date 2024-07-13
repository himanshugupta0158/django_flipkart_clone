from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, related_name="user_profile", on_delete=models.CASCADE)
    phone_number1 = models.CharField(max_length=20, blank=True, null=True)
    phone_number2 = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(default="")
    birth_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=1000)

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
