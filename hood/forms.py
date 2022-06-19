from django.contrib.auth.models import User
from django.db.models import fields
from django.forms import ModelForm
from .models import Neighborhood, Post, Business, Profile



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

class AddNeighborhoodForm(ModelForm):
    class Meta:
        model = Neighborhood
        fields = ['name','location','description','manager_name','manager_number','manager_email','hospital_name','hospital_number','hospital_email','police_name','police_number','police_email','hood_pic']