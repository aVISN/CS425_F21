# Repo for VISN online application project

## Repo structure: 
```bash
# /srv/apps = VirtualEnv and Django project files:
# not all files listed here, just important ones to know for now: 
├── requirements.txt    # lists venv's installed packages for version control
|                       # created with 'pip freeze > requirements.txt'
├── venv/               # virutal environment for django project
└── visn/               # django project directory
    ├── db.sqlite3      # project database
    ├── manage.py*      # utility for project managment tasks
    ├── pages/          # pages app
    │   ├── admin.py    # used to register app models with admin site
    │   ├── models.py   # models are classes that map to database tables
    │   ├── templates/  # HTML FILES
    │   │   ├── about.html      # simple page example
    │   │   ├── base.html       # other templates inherit from base
    |   |   |                   # integrates Bootstrap5
    │   │   ├── home.html       # simple page with dynamic display 
    |   |   |                   # based on user and login status
    │   │   └── registration/   # templates related to user registration
    │   │       ├── login.html      # login form
    │   │       └── register.html   # registration form
    │   ├── urls.py     # maps URL requests to views
    │   └── views.py    # functions and classes that serve responses to requests
    ├── static/         # static files collected to be served directly by Nginx
    |                   # collect with 'django-admin collectstatic' 
    └── visn/           # project settings directory
        ├── settings.py # list of installed apps, project wide settings 
        └── urls.py     # project url mappings (includes app urls)

# /root = used for testing git setup and a place for git notes
├── hello_github/
│   └── README.md   # branch setup 
└── README.md       # git/github setup

# /.gitignore = system wide ignore config to select directories for repo

# /etc/nginx = NGINX config files
├── sites-available/
│   └── default
├── sites-enabled/
    └── default -> /etc/nginx/sites-available/default

# /etc/uwsgi = uWSGI config files
├── apps-available/
│   └── visn.ini
├── apps-enabled/
    └── visn.ini -> /etc/uwsgi/apps-available/visn.ini

# /etc/systemd = uWSGI service
└── visn-uwsgi.service

# /var/www/html = NGINX html files
# used for testing nginx setup only
```
---

## Current project workflows: 
- use the virtual environment to work on project: 
```bash
cd /srv/apps
source venv/bin/activate
# to exit virtual environment use:
deactivate
```
- venv isn't part of version control, if install new packages in venv, capture:
```bash
cd /srv/apps
# deactivate # if active 
pip freeze > requirements.txt
# push to repo 
```
- check Nginx and uWSGI (web server, application server):
```bash
systemctl status nginx
systemctl status uwsgi
```
- restart Nginx and uWSGI (stopping and starting provides better error output)
```bash
systemctl stop nginx
systemctl start nginx
systemctl stop uwsgi
systemctl start uwsgi
# but can use restart
systemctl restart nginx 
systemctl restart uwsgi
```
- when Nginx and uWSGI running properly, can view pages at localhost in web browser

- Django dev server: shouldn't be used in production, but simplifies testing
```bash
cd /srv/apps
source venv/bin/activate
cd visn
./manage.py runserver
# can view pages at localhost:8000 in web browser
# to stop dev server, in terminal:
CTRL-C
```

---
## Projct setup* notes: 
**Note that VM images posted to team drive on 11/13/21 and 11/23/21 already have the following installations and configurations completed.*

### 1. Use VirtualBox* to create a Debian 11 VM (with a desktop) 

- login to desktop as root, open a terminal:
```bash
apt update
# will need these later
apt install vim curl tree
```

### 2. See /etc/nginx/README.md for basic NGINX install and setup walkthrough

### 3. See /srv/apps/README.md for VirtualEnv and Django project setup walkthrough

### 4. See /root/README.md for git and github setup walkthrough and git notes

### 5. See /etc/uwsgi/README.md for uWSGI and NGINX configuration to serve django project

### 6. See /root/hello_github/README.md* for walkthrough on setting up personal development branch
      *NOTE: currently on main-S branch, not main branch! 
      View on github by selecting main-S branch from drop down button or use address:
      github.com/aVISN/CS425_F21/tree/main-S/root/hello_github
---
---
#### *VirtualBox setup details:
---
- ENABLE CLIBOARD:

    ```
    in VM menu: Devices > Shared Clipboard > Bidirectional
    ```
---
- FIX RESOLUTION:

    - desktop:

        ```  
        click Devices (in VM window menu) > Insert Guest Additions CD Image.
	    Mount the CD-ROM: 
            mount /dev/cdrom /media/cdrom
	    Change into the mounted directory: 
            cd /media/cdrom
	    Install dependencies: 
            apt install -y dkms build-essential linux-headers-$(uname -r).
	    Install Guest Additions package:
            ./VBoxLinuxAdditions.run --nox11
	    Allow the installation to complete, reboot

	    login to desktop, click View (in VM window menu) 
            > Auto-Resize Guest Display (twice)
        ```
    - for ttys: (if you only use desktop, dont need this): 
    
        ```
        Reboot into GRUB menu. Press c key to enter GRUB’s command line. 
	        grub> set pager=1
	        grub> vbeinfo
	    note resolution desired, 
        enter 'normal' to continue with normal server boot

	    login as root, apt install vim 
	    edit /etc/default/grub to include the following settings:

            GRUB_CMDLINE_LINUX_DEFAULT="vga=792" 
        
        # (792==1024x768, search for grub vga values, not all in vbeinfo supported)
        reboot
	```

