# This is where Django projects are stored

# File sharing page development process 

Example of development steps from simple page to function based views to generic class-based views that uses models and forms. 

## 1. Setup basic view, url, template: 

Starting with a function based view lets us figure out the logic. We'll eventually turn this into a generic class-based view. Also setup media directory for uploaded files and configured to serve with nginx. 

vim pages/views.py: 
```
from django.core.files.storage import FileSystemStorage

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
```

then we need to update urls.py:
```
from .views import ... #HomePageView, FilesPageView, (commented out FilesPageView for now)
from . import views
from django.conf import settings
from django.conf.urls.static import static

# update path view: 
#    path('files/', FilesPageView.as_view(), name='files'),
    path('files/', views.files, name='files'),

# after urlpatterns list, add: 
# for use in development only, need to update for production:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

update files.html: 
```
<!-- removed div style -->
<div class="col-md-10"> 
  
  <h2>**List of Files Webpage**</h2>
  
  <form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    <input type="file" name="upload">
    <button type="submit">Upload file</button>
  </form>
  
  {% if url %}
    <p>Uploaded file: <a href="{{ url }}">{{ url }}</a></p>
  {% endif %}

</div> 
```

files uploaded by users are called "media" by Django, set media root/url:
vim visn/visn/settings.py
```
MEDIA_URL = '/files/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

update nginx to serve media files
vim /etc/nginx/sites-available/default:
```
	location /media/ { 
            alias /srv/apps/visn/media/; 
        } 
```
---
## 2. Adding a model and form, create upload page / file list page

Create a model to store file infomation in the database: 
pages/models.py
```
from django.db import models

# Create your models here.

class Upload(models.Model):
    description = models.CharField(max_length=100)
    comments = models.TextField(blank=True)
    filename = models.FileField(upload_to='')

    def __str__(self):
        return self.description
```

After changing models need to makemigrations and migrate to db:
```
./manage.py makemigrations
./manage.py migrate
```

Create a form for users to upload files / store info to model in db: 
/pages/forms.py
```
from django import forms

from .models import Upload

class UploadForm(forms.ModelForm):
    class Meta: 
        model = Upload
        fields = ('description', 'comments', 'filename')
```

Update views to use model and form:
pages/views.py
```
from django.shortcuts import render, redirect
...

from .forms import UploadForm
from .models import Upload

...

def files(request):
    files = Upload.objects.all()
    return render(request, 'files.html', {
        'files': files
    })

def upload(request):
    if request.method == 'POST':
        upload = UploadForm(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('files')
    else: 
        upload = UploadForm()
    return render(request, 'upload.html', {
        'form': upload
    })
```

Update files page ( -> list of files)
pages/templates/files.html: 
```
  <h2>**List of Files Webpage**</h2>

  <p>
    <a href="{% url 'upload' %}" class="btn btn-success">Upload file</a>
  </p>


  <table class="table table-hover table-responsive p-4">
    <thead>
      <tr>
        <th style="width: 30%">Description</th>
        <th style="width: 40%">Comments</th>
        <th style="width: 5%">Download</th>
      </tr>
    </thead>
    <tbody>
      {% for file in files %}
        <tr>
          <td>{{ file.description }}</td>
          <td>{{ file.comments }}</td>
          <td>
            <a href="{{ file.filename.url }}" class="btn btn-success" target="_blank">
              {{ file.filename }}
            </a>
          </td>
        <tr>
      {% endfor %}
    </tbody>
  </table>
```

Create upload form page: 
pages/templates/upload.html
```
{% extends 'base.html' %}
{% load crispy_forms_tags %}


{% block content %}
{% include 'header.html' %}
{% include 'sidebar.html' %}

<div class="col-md-10 p-5" >
  
  <h2>**Upload**</h2>
  <form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form|crispy }}
    <button type="submit">Upload file</button>
  </form>

</div> 

{% endblock content %}
```

Add upload page to urls
pages/urls.py
```
    path('files/upload/', views.upload, name='upload'), 
```

---
## 3. Update from function based views to generic class based views

Update function based to generic class based views: 
pages/views.py
```    
from django.views.generic import TemplateView, CreateView, ListView
...

class FilesPageView(ListView):
    model = Upload
    template_name = 'files.html'
    context_object_name = 'files'

class UploadFilesView(CreateView):
    model = Upload
    form_class = UploadForm
    success_url = reverse_lazy('files')
    template_name = 'upload.html'
```

update urls to use new views
pages/urls.py
```
from .views import AboutPageView, ProjectsPageView, ChatPageView, RegisterView, DashboardView, FilesPageView, UploadFilesView #HomePageView, 
...

    path('files/', FilesPageView.as_view(), name='files'),
    path('files/upload/', UploadFilesView.as_view(), name='upload'),
```

---

# Note: project setup still listed below, but adding notes from discord 
on current general use tips here (since installation/setup already configured in provided VM)

## * Django is now served through nginx, should be able to view pages in web browser 
at localhost addresses such as localhost (main page) or localhost/login

## Example: adding a page to the project's pages app:

1. add a template (.html file)
```bash
# within the project's pages app at /srv/apps/visn/pages 
# there is a templates directory that contains the base.html, home.html, and about.html pages
# can create a new page such as dashboard.html will inherit from base.html, 
# see how to set up by looking at both base.html and home.html
```
2. add a view to the app's views.py file
```bash
# create a line in the /srv/apps/visn/pages/views.py file for the new page, 
# something just like what is used for the home.html page: 
class HomePageView(TemplateView):
    template_name = 'home.html'
```
3. add url to the app's urls.py file
```bash
# create the url mapping in the /srv/apps/visn/pages/urls.py file for the new page, 
# something like what is used for the about page view: 
    path('about/', AboutPageView.as_view(), name='about'),
```

## Note, not everything will be added in pages app! 
We will want to create apps for other functionalities such as an app for chat 
and and app for file sharing, but creating a page is a good way to get started
with using Django

## Other pages or more sophisticated versions of our current templates
will need to interact with the database through ORM models, this example does
not go into models, will provide another example to illustrate integration of models

---

# 1. Basic Django installation and project setup: 

## 1. Create a virtual environment for project code: 
```bash
apt install python3-pip virtualenv
cd /srv
mkdir apps
cd apps
virtualenv -p python3 venv
```
## 2. Activate virtual environment
```bash
source venv/bin/activate # you can tell you are in the virtual environment b/c of prompt prefix
```
## 3. Install Django in virtual environment
```bash
pip install django
```
## 4. Create Django project 
```bash
django-admin startproject visn
# check with Django dev server:
cd visn
python manage.py runserver
    # use localhost:8000 in web browser address bar 
    # there will be a warning about 18 unapplied migrations: 
    # The program's settings.py file contains program settings, 
    # including a list of common Django applications that are added by default. 
    # The project also contains a models.py file where data models are defined. 
    # Each data model is mapped to a database table. 
    # To complete the project setup, we need to create the tables associated with 
    # the models of the applications listed in INSTALLED_APPS. 
    # Django includes a migration system that manages this. 
    # First stop the local server with the command CTRL-C and then run:
python manage.py makemigrations
    # makemigrations was actually done with project creation, 
    # but normally we need to makemigrations first before migrating them. 
python manage.py migrate 
# Django has created a SQLite database and migrated its built-in apps into the new file db.sqlite3
# now when check with the dev server, no errors: 
python manage.py runserver
# (check in web browser localhost:8000
# CTRL-C in terminal to stop server
```

# 2. Create a project application: 

## 1. Start an application
```bash
# lets create an app for static pages
python manage.py startapp pages
# update the project settings.py to include our app:
vim visn/settings.py 
# add to INSTALLED_APPS list: 
'pages', # and save file
```
- check for errors with app install with dev server
```bash
python manage.py runserver # localhost:8000 in web browser
CTRL-C # to stop server

## 2. Create app templates, urls, views
```
- now lets navigate into the app directory
```bash
cd pages
# create a templates directory
mkdir templates
# we will create a base html page that will be reused by other pages
vim templates/base.html
# add the following and save
<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>

<header>

  <a href="{% url 'home' %}">Home</a> | <a href="{% url 'about' %}">About</a>

</header>

<body>
  {% block content %}
  {% endblock content %}
</body>
</html>

```
- lets create home and about pages that inherit from the base page: 
```bash
vim templates/home.html # add and save:
{% extends 'base.html' %}

{% block content %}
<h1>Homepage</h1>
{% endblock content %}
```
```bash

vim templates/about.html # add and save: 
{% extends 'base.html' %}

{% block content %}
<h1>About page</h1>
{% endblock content %}
```
- now we need to modify the urls.py files at the project and app levels
```bash
vim /srv/apps/visn/visn/urls.py
# add include to the from django.urls line at top of file: 
from django.urls import path, include
# add the following to the urlpatterns list: 
path('', include('pages.urls')),
# save file
```
```bash
# create app level urls.py file (in /srv/apps/visn/pages directory)
vim urls.py
from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]
```
- now we need to update our app's view.py file:
```bash
vim views.py # add the following and save: 

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'
```
- now we can navigate back up to our project directory and run the dev server to test
```bash
cd ..
manage.py runserver
# in your web browser navigate to localhost:8000 and localhost:8000/about, try links
CTRL-C # to stop server
```

# 3. Add login/logout to pages app with Django's builtin user authentication system
- the auth app is istalled in new projects by default, see visn/settings.py INSTALLED_APPS list
- to use the app, we need to add it to our apps's urls.py file: 
```bash
vim pages/urls.py
# add include to the from django.urls line at top of file: 
from django.urls import path, include
# add the following line to the urlpatterns list and save
path('accounts/', include('django.contrib.auth.urls')),
```
- this not only created accounts/, but enabled a bunch of other URLS
- to see them, run the dev server:
```bash
./manage.py runserver
# in your web browser navigate to localhost:8000/accounts/
# since we have debug on, instead of a 404, django outputs a list of URLs it tried
# the auth app created lots of views and enabled urls for us by default:  
    # accounts/ login/ [name='login']
    # accounts/ logout/ [name='logout']
    # accounts/ password_change/ [name='password_change']
    # accounts/ password_change/done/ [name='password_change_done']
    # accounts/ password_reset/ [name='password_reset']
    # accounts/ password_reset/done/ [name='password_reset_done']
    # accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
    # accounts/ reset/done/ [name='password_reset_complete'] 
```
- but if we put localhost/accounts/login into our web browser
- we see that we still need to create the templates for these views
- we already have a templates directory for our app 
- the auth app looks for a template directory called registration
```bash
cd pages/templates
mkdir registration 
# create a login html file in the registration directory
vim registration/login.html
# add the following and save: 
{% extends 'base.html' %}

{% block content %}

<h2>Log In</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Log In</button>
</form>

{% endblock content %}
```
- check implementation with dev server: 
```bash
cd /srv/apps/visn
./manage.py runserver
# enter localhost:8000/accounts/login in browser address bar
CTRL-C # to stop server
```

# 4. cleanup urls
- I would rather login be at localhost/login than localhost/accounts/login
- edited path in pages/urls.py to: 
```bash
path('', include('django.contrib.auth.urls')),
```
- all the extra urls are still there, test with dev server:
```bash
./manage.py runserver # check localhost:8000/login in web browser
```

# 5. Create a registration page
- the Django auth app provided built-in urls and views for login, we only need to add a template
- but for registration we need to create our own view and url

- now we can create an html file in our pages templates registration directory
```bash 
vim pages/templates/registation/register.html
# add the following and save: 
{% extends 'base.html' %}

{% block content %}
<h2>Create an Account</h2>
<form method="POST">
	{% csrf_token %}
	{{ form.as_p }}
	<button type="submit">Register</button>
    </form>
{% endblock content %}

{% extends 'base.html' %}
```
- now we can add our view function:
```bash
vim pages/views.py
# update to the following and save: 
rom django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'templates/register.html'
```
- finally we add a url: 
```bash
vim pages/urls.py
# add the following to urlpatterns list and save:
path('register/', RegisterView.as_view(), name='register'),
```
# 6. Link everything together
- lets update our homepage to signify if user is logged in or not
- and add links to login (if not) and register, or logout (if logged in)
```bash
# vim pages/templates/home.html

{% extends 'base.html' %}

{% block content %}
<h1>Homepage</h1>
{% if user.is_authenticated %}
    Hi {{ user.username }}!
    <p><a href="{% url 'logout' %}">Log Out</a></p>
{% else %}
    <p>You are not logged in</p>
    <p><a href="{% url 'login' %}">Log In</a> or <a href="{% url 'register' %}">Register</a></p>
{% endif %}
{% endblock content %}
```
- lets also add links from our login and registration pages to each other
```bash
vim pages/templates/registration/login.html
# update to include Register link
{% extends 'base.html' %}

{% block content %}

<h2>Log In</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <p>No account? <a href="/register">Register</a></p>
  <button type="submit">Log In</button>
</form>

{% endblock content %}
```
```bash
vim pages/templates/registration/registration.html
# update to include Login link
{% extends 'base.html' %}

{% block content %}
<h2>Create an Account</h2>
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <p>Already have an account? <a href="/login">Log In</a></p>
    <button type="submit">Register</button>
</form>
{% endblock content %}
```
# 7. Add Bootstrap to forms with crispy forms:
- lets install a pip package called crispy forms which does some nice styling of our forms for us
```bash
pip install django-crispy-forms crispy-boostrap5
```
- Now that we have installed crispy we need to add the following into settings.py to configure what css framework it will use:
```bash
# add to INSTALLED_APPS list: 
'crispy_forms', 
'crispy_bootstrap5',
# add to bottom of doc: 
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'
```
```bash
# update login.html:
{% extends 'base.html' %}
{% load crispy_forms_tags %}

{% block content %}

<h2>Log In</h2>
<form method='POST'>
  {% csrf_token %}
  {{ form|crispy }}
  <p>No account? <a href='/register'>Register</a></p>
  <button type='submit'>Log In</button>
</form>

{% endblock content %}
```
```bash
# and register.html
{% extends 'base.html' %}
{% load crispy_forms_tags %}

{% block content %}
<h2>Create an Account</h2>
<form method="POST">
    {% csrf_token %}
    {{ form|crispy }}
    <p>Already have an account? <a href="/login">Login</a></p>
    <button type="submit">Register</button>
</form>
{% endblock content %}
```


