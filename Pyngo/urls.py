from django.urls import path
from .views import index, contact,services, all_notifications, about_us, contact_us, language

app_name = 'pyngo'

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('services/', services, name='services'),
    path('all/notifications/', all_notifications, name='all_notifications'),
    path('about/us/', about_us, name='about_us'),
    path('contact/us/', contact_us, name='contact_us'),
    path('language/<str:lang>/', language, name='language'),
]
