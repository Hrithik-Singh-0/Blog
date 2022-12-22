from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name = 'hompage'),
    path('create/', views.create, name = 'create'),
    path('delete/<str:Name>', views.delete, name='delete'),
]