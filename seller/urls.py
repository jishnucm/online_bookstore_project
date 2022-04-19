from django.urls import path
from .import views

urlpatterns = [
    path('admin6/', views.home, name="home"),
    path('admin7/', views.addbook, name="add"),
     path('admin8/', views.product, name="product"),
     path('admin9/', views.edit, name="edit"),
]