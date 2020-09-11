from django.shortcuts import render, redirect
from gallery.forms import (
    UserForm,
    UserProfileForm,
    UserPostForm,
    EditProfileForm,

)
from gallery.models import Post, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


def gallery(request):
    if User.is_authenticated:
        template = 'pages/login.html'
    else:
        template = 'pages/main.html'
    context = {'page_title': 'WebGallery'}
    return render(request, template, context)


@login_required
def home(request):
    private = Post.objects.private_posts(user=request.user)
    queryset = private.all()
    context = {'page_title': 'Home', 'querysets': queryset}
    return render(request, 'pages/home.html', context)


@login_required
def profile(request):
    context = {'page_title': 'Profile'}
    return render(request, 'pages/profile.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        edit_form = EditProfileForm(request.POST, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('/profile')
    else:
        edit_form = EditProfileForm(instance=request.user)
    context = {'edit_form': edit_form}
    return render(request, 'pages/edit_profile.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        pass_form = PasswordChangeForm(data=request.POST, user=request.user)
        if pass_form.is_valid():
            pass_form.save()
            update_session_auth_hash(request, pass_form.user)
            return redirect('/profile')
    else:
        pass_form = PasswordChangeForm(user=request.user)
    context = {'pass_form': pass_form}
    return render(request, 'pages/change_password.html', context)


@login_required
def delete_post(request, post_id=None):
    private = Post.objects.private_posts(user=request.user)
    queryset = private.get(id=post_id)
    queryset.delete()
    return HttpResponseRedirect(reverse('gallery:home'))


@login_required
def detail(request, post_id):
    private = Post.objects.private_posts(user=request.user)
    queryset = private.get(pk=post_id)
    context = {'page_title': 'test', 'queryset': queryset}
    return render(request, 'pages/detail.html', context)


@login_required
def createpost(request):
    if request.method == 'POST':
        post_form = UserPostForm(request.POST, request.FILES)
        if post_form.is_valid():
            obj = post_form.save(commit=False)
            obj.user = request.user
            obj.save()
            return HttpResponseRedirect(reverse('gallery:home'))
    else:
        post_form = UserPostForm()
    context = {'page_title': 'Add image', 'post_form': post_form}
    return render(request, 'pages/add_img.html', context)


def user_login(request):
    context = {'page_title': 'Login'}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                # Here redirect to user page with home.html
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
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered,
        'page_title': 'Register'
    })


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('gallery:gallery'))
