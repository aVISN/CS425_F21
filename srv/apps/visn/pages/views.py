# docs:
# function-based views: https://docs.djangoproject.com/en/3.2/topics/http/views/
# class-based views: https://docs.djangoproject.com/en/3.2/ref/class-based-views/
# classy class-based views: https://ccbv.co.uk/

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView, FormView
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage
from .forms import UploadForm
from .models import Upload

#class HomePageView(TemplateView):
#    template_name = 'home.html'

#class AboutPageView(TemplateView):
#    template_name = 'about.html'

class RegisterView(CreateView):
    form_class = UserCreationForm
    # generic class based views need reverse_lazy instead of reverse for urls
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

class DashboardView(TemplateView):
    template_name = 'dashboard.html'
    
class ProjectsPageView(TemplateView):
    template_name = 'projects.html'
    
class ChatPageView(TemplateView):
    template_name = 'chat.html'

class NetworkPageView(TemplateView):
    template_name = 'network.html'

class ToolsPageView(FormView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('tools')
    template_name = 'tools.html'
    def get_form_kwargs(self):
        kwargs = super(ToolsPageView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class FilesPageView(ListView):
    model = Upload
    template_name = 'files.html'
    context_object_name = 'files'

class UploadFilesView(CreateView):
    model = Upload
    form_class = UploadForm
    success_url = reverse_lazy('files')
    template_name = 'upload.html'
