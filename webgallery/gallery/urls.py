from django.urls import path
from gallery import views

urlpatterns = [
    path('', views.gallery, name="gallery"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
]
