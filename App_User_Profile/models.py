from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    contact_number = models.CharField(max_length=10)
    email = models.EmailField(unique=True, max_length=50)
    profile_picture = models.ImageField(upload_to='Profile_Pics/', null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
