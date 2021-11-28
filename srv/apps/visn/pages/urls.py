from django.urls import path, include
from .views import HomePageView, AboutPageView, ProjectsPageView, FilesPageView, ChatPageView, RegisterView, DashboardView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view()),
    path('', include('django.contrib.auth.urls')),
    path('home/', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('projects/', ProjectsPageView.as_view(), name='projects'),
    path('files/', FilesPageView.as_view(), name='files'),
    path('chat/', ChatPageView.as_view(), name='chat'),
    path('register/', RegisterView.as_view(), name='register'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
