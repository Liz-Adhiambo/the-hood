from django.contrib import admin
from .models import  Business, Neighborhood, Post, PostType, Profile


admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Neighborhood)
admin.site.register(Business)
admin.site.register(PostType)