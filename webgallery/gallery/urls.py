from django.urls import path
from gallery import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'gallery'
urlpatterns = [
    path('', views.gallery, name="gallery"),
    path('login/', views.user_login, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.user_logout, name="logout"),
    path('home/', views.home, name="home"),
    path('add_img/', views.createpost, name="add_img"),
    path('detail/', views.detail, name="detail"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)