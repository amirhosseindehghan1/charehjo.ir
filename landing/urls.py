from django.urls import path
from .views import discovery


urlpatterns = [
    path('', discovery),
    ]