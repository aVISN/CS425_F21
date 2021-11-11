from django.urls import path, include
from .views import HomePageView, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('accounts/', include('django.contrib.auth.urls')),
]
