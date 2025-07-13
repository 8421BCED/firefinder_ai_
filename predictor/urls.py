from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('simulate/', views.simulate, name='simulate'),
]
