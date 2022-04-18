from django.urls import path
from .import views

urlpatterns = [
    path('admin2/', views.home),
    path('admin3/', views.books, name="books"),
     path('admin4/', views.payment, name="payment"),
]
