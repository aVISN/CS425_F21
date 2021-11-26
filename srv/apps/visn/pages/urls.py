from django.urls import path, include
from .views import LoginPageView, HomePageView, AboutPageView, RegisterView, DashboardView

urlpatterns = [
    path('', LoginPageView.as_view(), name='home'),
    path('', HomePageView.as_view(), name='home'),
    path('', include('django.contrib.auth.urls')),
    path('about/', AboutPageView.as_view(), name='about'),
    path('register/', RegisterView.as_view(), name='register'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
