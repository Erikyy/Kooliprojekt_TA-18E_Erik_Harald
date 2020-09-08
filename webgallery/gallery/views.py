from django.shortcuts import render

def gallery(request):
    context = { 'page_title': 'Main Page'}
    return render(request, 'pages/main.html', {})


def login(request):
    context = { 'page_title': 'Login'}
    return render(request, 'pages/login.html', {})

def register(request):
    context = { 'page_title': 'Register'}
    return render(request, 'pages/register.html', {})
