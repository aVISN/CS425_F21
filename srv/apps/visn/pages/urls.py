from django.urls import path, include
from .views import HomePageView, AboutPageView, RegisterView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('', include('django.contrib.auth.urls')),
    path('about/', AboutPageView.as_view(), name='about'),
    path('register/', RegisterView.as_view(), name='register'),
]
