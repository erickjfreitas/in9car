from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, cadastre

urlpatterns = [
    path('', views.home),
    path('login/', LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name="logout")
   


]
