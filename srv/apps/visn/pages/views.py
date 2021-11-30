from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage


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
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['upload']
        f = FileSystemStorage()
        name = f.save(uploaded_file.name, uploaded_file)
        context['url'] = f.url(name)
    return render(request, 'files.html', context)    
