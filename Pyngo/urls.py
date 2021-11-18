from django.urls import path
from .views import index, contact,services, all_notifications

app_name = 'pyngo'

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('services/', services, name='services'),
    path('all/notifications/', all_notifications, name='all_notifications'),
]
