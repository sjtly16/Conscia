from django.urls import path
from .views import LoginAPI

urlpatterns = [
    path('auth/login', LoginAPI.as_view(), name="login"),

]
