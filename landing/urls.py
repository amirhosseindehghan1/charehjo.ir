from django.urls import path
from .views import discovery, market, develop_and_launch


urlpatterns = [
    path('', discovery),
    path('market/', market),
    path('market/', develop_and_launch),
    ]