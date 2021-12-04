# docs: https://docs.djangoproject.com/en/3.2/topics/http/urls/

from django.urls import path, include
from .views import ProjectsPageView, ChatPageView, RegisterView, DashboardView, FilesPageView, ToolsPageView, UploadFilesView #HomePageView, AboutPageView,  
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', auth_views.LoginView.as_view()),
    path('', include('django.contrib.auth.urls')),
#    path('home/', HomePageView.as_view(), name='home'),
#    path('about/', AboutPageView.as_view(), name='about'),
    path('projects/', ProjectsPageView.as_view(), name='projects'),
    path('chat/', ChatPageView.as_view(), name='chat'),
    path('register/', RegisterView.as_view(), name='register'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('files/', FilesPageView.as_view(), name='files'),
    path('tools/', ToolsPageView.as_view(), name='tools'),
    path('files/upload/', UploadFilesView.as_view(), name='upload'),
]


# for use during development only, need to remove for production: 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
