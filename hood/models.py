from datetime import datetime
from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField


User = get_user_model()

# User profile model
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profile_image=CloudinaryField('image', blank=True)
    date_joined=models.DateTimeField(default=datetime.now)
    
    
    

    def __str__(self):
        return self.user.username