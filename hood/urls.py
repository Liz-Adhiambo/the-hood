from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('feed/', views.feed, name='feed'),
    path('businesses/', views.businesses, name='businesses'),
    path('neigborhood/', views.neighborhood, name='neighborhood'),
    path('search_businesses/', views.search, name='search'),
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),

    
]