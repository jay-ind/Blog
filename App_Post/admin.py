from django.contrib import admin
from .models import TblPost


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['owner', 'title', 'description', 'thumbnail_image', 'timestamp', 'id']


admin.site.register(TblPost, PostAdmin)
