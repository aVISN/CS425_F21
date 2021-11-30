from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
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

#class FilesPageView(TemplateView):
#    template_name = 'files.html'

def files(request):
    files = Upload.objects.all()
    return render(request, 'files.html', { 'files': files })

def upload(request):
    if request.method == 'POST':
        upload = UploadForm(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('files')
    else: 
        upload = UploadForm()
    return render(request, 'upload.html', { 'form': upload })


