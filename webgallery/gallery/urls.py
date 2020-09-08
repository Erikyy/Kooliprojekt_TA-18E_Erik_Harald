from django.urls import path
from gallery import views

app_name = 'gallery'
urlpatterns = [
    path('', views.gallery, name="gallery"),
    path('login/', views.user_login, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.user_logout, name="logout"),
]
