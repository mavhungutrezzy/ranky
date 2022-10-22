from django.urls import path

from . import views

urlpatterns = [
    path('accounts/signin/', views.signin, name='signin'),
    path('accounts/logout/', views.logout, name='logout'),
    path('accounts/register/', views.register, name='register'),
]