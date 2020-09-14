from django.urls import path
from gallery import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'gallery'
urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.user_login, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.user_logout, name="logout"),
    path('images/', views.home, name="images"),
    path('images/<int:post_id>/', views.detail, name="detail"),
    path('images/<int:post_id>/delete/', views.delete_post, name='delete'),
    path('images/<int:post_id>/edit/', views.edit_post, name='delete'),
    path('gallery/', views.gallery, name="gallery"),
    path('gallery_column/', views.gallery_column, name="gallery_column"),
    path('gallery_full', views.gallery_full, name="gallery_full"),
    path('search', views.search, name="search"),
    path('add_img/', views.createpost, name="add_img"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('password/', views.change_password, name="change_password"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
