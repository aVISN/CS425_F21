# Views are basically functions that define how to respond to http requests. 
# In django we can create function based views, class based views, or use 
# generic class based views provided by Django.
# We are generally using classes and importing generic views from django. 

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
from django.contrib.auth.models import User

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

class ClientsPageView(ListView):
    model = User
    template_name = 'clients.html'
    context_object_name = 'client_list'
    
class ProjectsPageView(TemplateView):
    template_name = 'projects.html'
    
class ChatPageView(TemplateView):
    template_name = 'chat.html'

class NetworkPageView(TemplateView):
    template_name = 'network.html'

class ToolsPageView(TemplateView):
    template_name = 'tools.html'

class PasswordChangePageView(FormView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('tools')
    template_name = 'registration/password_change.html'
    def get_form_kwargs(self):
        kwargs = super(PasswordChangePageView, self).get_form_kwargs()
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
