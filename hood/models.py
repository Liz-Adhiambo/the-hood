from datetime import datetime
from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField


User = get_user_model()
class Neighborhood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    description = models.TextField()
    manager_name = models.CharField(max_length=100, blank=True)
    manager_number = models.CharField(max_length=20, blank=True)
    manager_email = models.EmailField(blank=True)
    hospital_name = models.CharField(max_length=100, blank=True)
    hospital_number = models.CharField(max_length=20, blank=True)
    hospital_email = models.EmailField(blank=True)
    police_name = models.CharField(max_length=100, blank=True)
    police_number = models.CharField(max_length=20, blank=True)
    police_email = models.EmailField(blank=True)
    hood_pic = CloudinaryField('images', default='image/upload/v1627343010/neighborhood1_cj2fyx.jpg')

    @property
    def occupants_count(self):
        return Profile.objects.filter(neighborhood=self).count()

    def __str__(self):
        return self.name
    
    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)

    @classmethod
    def update_neighborhood(cls,id,name):
        return cls.objects.filter(id=id).update(name=name)








# User profile model
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile') 
    bio = models.TextField(blank=True)
    profile_image=CloudinaryField('image', blank=True)
    date_joined=models.DateTimeField(default=datetime.now)
    house = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    street = models.CharField(max_length=50,blank=True)
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.SET_NULL, null=True,related_name='neighbors',blank=True)


    def __str__(self):
        return self.user.username

class Business(models.Model):
    name=models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    start_day = models.CharField(max_length=50)
    end_day = models.CharField(max_length=50)
    open_time = models.CharField(max_length=50)
    close_time = models.CharField(max_length=50)
    bs_image = CloudinaryField('images')

    user=models.ForeignKey(Profile, on_delete=models.CASCADE) 
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls, business_id):
        return cls.objects.filter(id=business_id)

    @classmethod
    def update_business(cls,id,name):
        update = cls.objects.filter(id=id).update(name=name)
        return update

class PostType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=120, null=True)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post_image = CloudinaryField('imges')

    type = models.ForeignKey(PostType, on_delete=models.CASCADE, related_name='posts')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    hood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title

    @classmethod
    def search_post(cls, search_term):
        return cls.objects.filter(title__icontains=search_term).all()