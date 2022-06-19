from django.contrib.auth.models import User
from django.db.models import fields
from django.forms import ModelForm
from .models import Post, Business, Profile



class NewPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'post', 'type','post_image']

class NewBusinessForm(ModelForm):
    class Meta:
        model = Business
        exclude = ['user', 'neighborhood']

class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','bio','date_joined']

class ChangeNeighborhoodForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['neighborhood']