from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_name, name='index'),
    path('login', views.login_name, name='index')
]