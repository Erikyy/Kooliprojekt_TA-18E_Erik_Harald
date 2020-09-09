from django.shortcuts import render
from gallery.forms import UserForm, UserProfileForm, UserPostForm
from gallery.models import Post, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def gallery(request):
    context = { 'page_title': 'Main Page'}
    return render(request, 'pages/main.html', context)

def home(request):
    context = { 'page_title': 'Home' }
    return render(request, 'pages/home.html', context)

@login_required
def removepost(request):
    pass

def detail(request):
    pass

def createpost(request):
    
    if request.method == 'POST':
        post_form = UserPostForm(request.POST or None)
        if post_form.is_valid():
            
            instance = post_form.save(commit=False)
            
            post = Post()
            post.user = request.user
            post.post_img = request.FILES['post_img']
            post.save()
            #instance.post_img = request.FILES['post_img']
          
            
            #instance.save()
    else:
        post_form = UserPostForm()
    context = { 'page_title': 'Add image', 'post_form': post_form}
    return render(request, 'pages/add_img.html', context)


def user_login(request):
    context = { 'page_title': 'Login'}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            if user.is_active:
                login(request,user)
                #Here redirect to user page with home.html
                return HttpResponseRedirect(reverse('gallery:home'))
            else:
                return HttpResponse("Your account was inactive")
        else:
            return HttpResponse("Invalid login credentials")
    else:
        return render(request, 'pages/login.html', context)

def register(request):
    
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()


    return render(request, 'pages/register.html', {
                        'user_form':user_form,
                        'profile_form': profile_form,
                        'registered': registered,
                        'page_title': 'Register'
    })

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('gallery:gallery'))
