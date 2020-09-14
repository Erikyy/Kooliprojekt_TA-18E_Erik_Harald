from django.shortcuts import render, redirect
from gallery.forms import (
    UserForm,
    UserLoginForm,
    UserProfileForm,
    UserPostForm,
    EditProfileForm,
    EditPostForm,
)
from gallery.models import Post, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth import update_session_auth_hash
from django.db.models import Q


def get_post(user, id):
    return Post.objects.filter(user=user).get(id=id)


def get_all_posts(user):
    return Post.objects.filter(user=user).all()


@login_required
def home(request):
    queryset = get_all_posts(request.user)
    context = {'page_title': 'Your photos', 'queryset': queryset}
    return render(request, 'pages/images.html', context)


@login_required
def gallery(request):
    queryset = get_all_posts(request.user)
    context = {'page_title': 'Gallery', 'queryset': queryset}
    return render(request, 'pages/gallery.html', context)

@login_required
def gallery_column(request):
    queryset = get_all_posts(request.user)
    context = {'page_title': 'Gallery', 'queryset': queryset}
    return render(request, 'pages/gallery_column.html', context)


@login_required
def gallery_full(request):
    queryset = get_all_posts(request.user)
    context = {'page_title': 'Full screen', 'queryset': queryset}
    return render(request, 'pages/gallery_full.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        edit_form = EditProfileForm(request.POST, instance=request.user)
        profile = request.user.userprofile
        profile_form = UserProfileForm(
            request.POST, request.FILES, instance=profile)
        if edit_form.is_valid() and profile_form.is_valid():
            edit_form.save()
            profile_form.save()
            return redirect('/edit_profile')
    else:
        edit_form = EditProfileForm(instance=request.user)
        profile_form = UserProfileForm(request.POST)
    context = {'edit_form': edit_form, 'profile_form': profile_form}
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
    return render(request, 'pages/edit_password.html', context)


@login_required
def delete_post(request, post_id=None):
    obj = get_post(request.user, post_id)
    obj.delete()
    return redirect('gallery:home')


@login_required
def edit_post(request, post_id=None):
    obj = get_post(request.user, post_id)
    form = EditPostForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('gallery:detail', post_id=post_id)
    template_name = 'pages/edit_post.html'
    context = {'page_title': 'Edit post', 'post_form': form}
    return render(request, template_name, context)


@login_required
def detail(request, post_id):
    obj = get_post(request.user, post_id)
    context = {'page_title': 'test', 'object': obj}
    return render(request, 'pages/detail.html', context)


@login_required
def createpost(request):
    if request.method == 'POST':
        post_form = UserPostForm(request.POST, request.FILES)
        if post_form.is_valid():
            obj = post_form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('gallery:home')
    else:
        post_form = UserPostForm()
    context = {'page_title': 'Add image', 'post_form': post_form}
    return render(request, 'pages/add_img.html', context)


@login_required
def search(request):
    query = request.GET.get('q')
    if query:
        result = Post.objects.filter(Q(title__icontains=query) | Q(post_img__icontains=query))
        template = 'pages/images.html'
        context = {"queryset": result}
        return render(request, template, context)
    return redirect('gallery:home')
    


def user_login(request):
    if request.user.is_authenticated:
        return redirect('gallery:home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                # Here redirect to user page with home.html
                return redirect('gallery:home')
            else:
                return HttpResponse("Your account was inactive")
        else:
            return HttpResponse("Invalid login credentials")
    else:
        login_form = UserLoginForm()
        context = {'page_title': 'Login', 'login_form': login_form}
        return render(request, 'pages/login.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('gallery:home')
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
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
    return redirect('gallery:login')
