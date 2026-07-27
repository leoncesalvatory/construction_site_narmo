from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('projects/', projects, name='projects'),
    path('news-careers/', news_careers, name='news_careers'),
    path('contact/', contact, name='contact'),
    # Add detail views later, e.g., path('projects/<slug:slug>/', project_detail, name='project_detail'),
]