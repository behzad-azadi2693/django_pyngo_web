from django.urls import path
from .views import index 

app_name = 'pyngo'

urlpatterns = [
    path('', index, name='index')
]
