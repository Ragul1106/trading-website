from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.redirect_to_login, name="redirect"),
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name="login"),
    path('home/', views.home, name="home"),
    path('blog/', views.blog, name="blog"),
    path('about/', views.about_view, name="about"),
    path('logout/', views.user_logout, name="logout"), 
     path("partner/", views.partner, name="partner"),
     path("market-explorer/", views.market_explorer, name="market_explorer"),
     path("ready-tokens/", views.ready_token_list, name="ready_tokens"),
     path("options/", views.option_list, name="option_list"),
     path("file-check/", views.file_check, name="file_check"),
     path("faq/", views.faq_list, name="faq"),
      path("blogs/", views.blog_list, name="blogs"),
    path("blogs/<slug:slug>/", views.blog_detail, name="blog_detail"),
    path("docs/", views.docs_list, name="docs_list"),
    path("docs/<slug:slug>/", views.docs_detail, name="docs_detail"),
    path("presskit/", views.presskit_list, name="presskit"),
    path("investor/", views.investor_page, name="investor"),
     path("investor/apply/", views.apply_view, name="apply"), 
]
