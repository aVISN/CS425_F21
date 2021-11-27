from django.urls import path, include
from .views import LoginPageView, HomePageView, AboutPageView, ProjectsPageView, FilesPageView, ChatPageView, RegisterView, DashboardView

urlpatterns = [
    path('', LoginPageView.as_view(), name='home'),
#   path('', HomePageView.as_view(), name='home'),
    path('', include('django.contrib.auth.urls')),
    path('about/', AboutPageView.as_view(), name='about'),
    path('projects/', ProjectsPageView.as_view(), name='about'),
    path('files/', FilesPageView.as_view(), name='about'),
    path('chat/', ChatPageView.as_view(), name='about'),
    path('register/', RegisterView.as_view(), name='register'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
