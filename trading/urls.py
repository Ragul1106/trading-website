from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.redirect_to_login, name="redirect"),
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name="login"),
    path('home/', views.home, name="home"),
    path('logout/', views.user_logout, name="logout"), 
    path('about/', views.about_view, name="about"),
    path('blog/', views.blog, name="blog"),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
