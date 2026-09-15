from django.urls import path
from client import views

urlpatterns = [
    path('', views.home, name='home'),
    path("sign",views.sign,name="sign"),
    path("login",views.login,name="login"),
    path("download",views.download,name="download"),
]




