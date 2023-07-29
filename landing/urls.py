from django.urls import path
from .views import discovery, market


urlpatterns = [
    path('', discovery),
    path('', market),
    ]