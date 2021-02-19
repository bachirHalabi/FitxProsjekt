from django.urls import path
from . import views


urlpatterns = [
    path('signup', views.user_register, name='user_register'),

]