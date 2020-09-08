from django.shortcuts import render
from gallery.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
def gallery(request):
    context = { 'page_title': 'Main Page'}
    return render(request, 'pages/main.html', {})

def home(request):
    context = { 'page_title': 'Home' }
    return render(request, 'pages/home.html', {})


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
        return render(request, 'pages/login.html', {})

def register(request):
    context = { 'page_title': 'Register'}
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
                        'registered': registered
    })

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('gallery:gallery'))
