
from django.urls import  path
from .views import Cars,Brend
from .views import home,moshinalar


urlpatterns = [
    path('',home),
    path('cars/',moshinalar),
]