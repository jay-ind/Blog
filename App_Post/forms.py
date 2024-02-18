from django import forms
from App_User_Profile.models import Profile
from .models import TblPost


class PostForm(forms.ModelForm):
    class Meta:
        model = TblPost
        fields = ['title', 'description', 'thumbnail_image']

        widgets = {
            'title': forms.TextInput(attrs={
                'name': 'title',
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'name': 'description',
                'class': 'form-control',
            }),
            'thumbnail_image': forms.FileInput(attrs={
                'name': 'thumbnail_image',
                'class': 'form-control',
            }),
        }