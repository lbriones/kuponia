"""kuponia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from koupons.views import IndexView, CouponDetailView, favorite_coupon, user_profile, landing


urlpatterns = [
    url(r'^$', landing, name='landing'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^koupons/', include('koupons.urls')),
    url(r'^favorite_coupon/(\d+)/$', favorite_coupon, name='favorite_coupon'),
    url(r'^accounts/(?P<id>[\w-]+)/$', user_profile, name='user_profile'),


]
