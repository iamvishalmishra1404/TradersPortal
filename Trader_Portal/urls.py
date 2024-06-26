"""
URL configuration for Trader_Portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.contrib.auth import views as auth_views
from Userapp import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login , name= "login"),
    path('logout/',auth_views.LogoutView.as_view() , name='logout'),
    path('social-auth/',include('social_django.urls',namespace= 'social')),
    path('home/',views.home,name = 'home'),
    path('api/search/', views.CompanySearchAPIView.as_view(), name='company-search'),
    path('api/watchlist/', views.AddToWatchlistAPIView.as_view(), name='watchlist-create'),
    path('price/search/', views.GetPriceAPIView.as_view(), name='price-search'),

]
