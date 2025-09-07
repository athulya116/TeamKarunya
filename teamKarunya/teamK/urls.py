from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('gallery/', views.gallery, name='gallery'),
    path('about/', views.about, name= 'about'),
    path('contact/', views.contact, name='contact'),
    # path('404/', views.custom_404, name='custom_404'),
]


