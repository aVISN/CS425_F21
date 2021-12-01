from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage
from .forms import UploadForm
from .models import Upload

#class HomePageView(TemplateView):
#    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

class DashboardView(TemplateView):
    template_name = 'dashboard.html'
    
class ProjectsPageView(TemplateView):
    template_name = 'projects.html'
    
class ChatPageView(TemplateView):
    template_name = 'chat.html'

class FilesPageView(ListView):
    model = Upload
    template_name = 'files.html'
    context_object_name = 'files'

class UploadFilesView(CreateView):
    model = Upload
    form_class = UploadForm
    success_url = reverse_lazy('files')
    template_name = 'upload.html'
