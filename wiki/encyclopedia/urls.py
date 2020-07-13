from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("random", views.random, name="random"),
    path("search/<str:query>", views.search, name="search")
]
