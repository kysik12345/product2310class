from .views import *
from django.urls import path
from users.views import register,login,logout

urlpatterns = [
    path("register/",register, name='register'),
    path("login/", login, name='login'),
    # path("change_password/", change_password, name='change_password'),
    path("logout/", logout, name='logout'),
]