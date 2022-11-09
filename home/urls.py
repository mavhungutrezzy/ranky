from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("detail/<int:place_id>", views.detail, name="detail"),
    path("add_comment/<int:place_id>", views.add_comment, name="add_comment"),
]
