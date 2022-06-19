from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from.models import Profile
from . import models
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm, NewBusinessForm, EditProfileForm, ChangeNeighborhoodForm
# Create your views here.


def index(request):

    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, first_name=first_name,last_name=last_name, email=email, password=password)
                user.save()

                #log user in and redirect to settings page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                #create a Profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('signin')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
        
    else:
         return render(request,'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signin')

    else:
        return render(request, 'signin.html')


@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')


def feed(request):
    current_user = request.user.profile
    posts = models.Post.objects.filter(hood=current_user.neighborhood)

    if request.method == 'POST':
        new_post_form = NewPostForm(request.POST)
        if new_post_form.is_valid():
            new_post_form.instance.user = current_user
            new_post_form.instance.hood = current_user.neighborhood
            new_post_form.save()

            return redirect('feed')
    else:
        new_post_form = NewPostForm()

    title = 'Feed'
    context = {
        'title': title,
        'posts': posts,
        'new_post_form': new_post_form,
    }

    return render(request, 'feed.html',context)

def businesses(request):
    current_user = request.user.profile

    if request.method == 'POST':
        new_business_form = NewBusinessForm(request.POST)
        if new_business_form.is_valid():
            new_business_form.instance.user = current_user
            new_business_form.instance.neighborhood = current_user.neighborhood
            new_business_form.save()

            return redirect('businesses')
    else:
        new_business_form = NewBusinessForm()

    businesses = models.Business.objects.filter(neighborhood=current_user.neighborhood)

    title = 'Businesses'
    context = {
        'title': title,
        'businesses':businesses,
        'new_business_form':new_business_form,
    }

    return render(request, 'business.html', context)


def neighborhood(request):

    current_user = request.user
    neighborhood = current_user.profile.neighborhood

    
    
    title = 'Neighborhood'
    context = {
        'title': title,
        'neighborhood': neighborhood,
    }

    return render(request, 'hood.html', context)

def profile(request):

    if request.method == 'POST':
        edit_profile_form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        change_neighborhood_form = ChangeNeighborhoodForm(request.POST, request.FILES, instance=request.user.profile)
        if edit_profile_form.is_valid():
            edit_profile_form.instance.user = request.user
            edit_profile_form.save()

            redirect('profile')
        elif change_neighborhood_form.is_valid():
            change_neighborhood_form.save()

            redirect('profile')

    else:
        edit_profile_form = EditProfileForm()
        change_neighborhood_form = ChangeNeighborhoodForm()

    title = 'Profile'
    context = {
        'title': title,
        'edit_profile_form': edit_profile_form,
        'change_neighborhood_form':change_neighborhood_form,
    }

    return render(request, 'profile.html', context)