
from django.urls import path
from .import views
urlpatterns = [
    path('h', views.Hello, name='Hello'),
    path('w', views.World, name='World'),
    path('a', views.Welcome, name='Welcome'),



 ]