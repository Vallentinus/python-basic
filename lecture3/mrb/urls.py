from django.urls import path
from . import views

urlpatterns =[
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("kex", views.kex, name="kex"),
    path("penes", views.penes, name="penes")
]