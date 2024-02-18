from django.db import models
from App_User_Profile.models import Profile


# Create your models here.

class TblPost(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=500)
    description = models.TextField()
    thumbnail_image = models.ImageField(upload_to='Thumbnail_Images/', null=True, blank=True)
    timestamp = models.DateField(auto_now_add=True)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title
