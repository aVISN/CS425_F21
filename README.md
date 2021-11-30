# Repo for VISN online application project

Overview of current project interaction: 
VM Installation, Git/Github setup, Creating a branch, Using branch, Merging with main. Project file overview, where to update .html files, how to check with dev server and web server. Merging branches with main project. 

---

## Install VM:

The VM was created with VirtualBox 6.1.26, using a different version of VB may cause errors. 

1. Download VitualBox 6.1.26 from https://www.virtualbox.org/wiki/Download_Old_Builds_6_1

2. Download and extract aVISNClone2.zip from Drive

3. Add VM to VirtualBox
	- Select Tools from the tops of VMs list in VirtualBox. 
	- Select Add button and navigate to where you saved folder (VB default on Windows is C:\Users\YourUsernameHere\VirtualBox VMs)
	- Select Start to boot the VM.

VM settings: 

```
vm login: 
    username: root
    password: bmo

django superuser: 
    username: admin
    password: visnpass

visn site user:
    username: test
    password: goodpass
```

## Setup git/github

4. Fix git credentials setup in VM images (I forgot to remove my creditials from this VM)

    ```bash
    Open a terminal: 
    # check
    git config --global user.name
    git congig --global user.email

    # remove my credentials
    cd ~
    vim .gitconfig
    # delete all lines under [user] tag 
    # save file

    # add you credentials
    git config --global user.name "Your name goes here"
    git config --global user.email "your email address goes here"
    # check
    git config --global user.name
    git congig --global user.email
    ```

5. Pull updates from repo to local branch (vm already has local branch and remote repo setup configured)

    ```bash
    # check local branch
    git status
    # check for remote updates
    git fetch
    # check updates with local
    git status
    # pull updates from remote to local
    # git pull
    # check
    git status
    ```

6. Create a personal development branch

    ```bash
    # create a new branch
    # -b option creates the branch if it does not exist and switches to it
    # command is git checkout -b nameOfNewBranchHere, I am using the name "main-S" ("main-{my first initial}")
    git checkout -b main-S # CHANGE 'S' to your initial!

    # check using new branch
    git status

    # create a test file and push to new branch
    cd ~/hello_github
    git status
    vim hello_branch.txt # add something to file
    git status
    git add .
    git status
    git commit -m "Testing git branch creation and use with Github"
    git push --set-upstream origin main-S # CHANGE 'S' to your initial!

    # note, after setting the upstream branch, can just use git push for subsequent commits to branch
    # edit hello_branch.txt again
    vim hello_branch.txt # add something else to file
    git status
    git add .
    git status
    git commit -m "Testing subsequent pushes to branch after initial upstream set "
    git push 
    ```

## Add code to an existing file:

7. Example: Adding html to a page

    > NOTE: whenever working on project, should be using project virtual environment:
    ```bash
    cd /srv/apps
    source venv/bin/activate
    # can exit virtual environment with: 
    deactivate
    ```
    There are already pages configured for Projects, Files, and Chat. If you wanted to update the html for the Chat page, you would work on the file /srv/apps/visn/pages/templates/chat.html

    Do not delete what is already there. Each page inherits a base file, header, and sidebar. Put your code above within the div column tag (i.e. replace **List of Files Webpage** with your html). Note, you should not add code such as <!DOCTYPE html>...<head>... everthing above the <body> tag is already accounted for in the base template - and the page footer comes after the {% endblock content %}, we only need to add the main content body to each of the pages. 
    
    ```bash
    # add something to chat.html, save 
    ```

8. Check updates with dev server and web server

    ```bash
    # check updates in dev server
    cd /srv/apps/visn
    ./manage.py runserver 
    # check localhost:8000/chat in your web browser
    # also check general site, localhost:8000, login, dashboard etc
    # Note any error messages such as 404 codes in output of dev server in terminal

    # check updates in web server
    systemctl restart nginx
    systemctl restart uwsgi
    # check localhost/chat in your web browser
    # also check general site, localhost, login, dashboard etc
    # can check logs at /var/log/nginx/access.log for errors
    ```

## Save updates to remote branch:

9. Push local branch updates to remote branch

    ```bash
    # check git status (and make sure on personal dev branch)
    git status
    # add updates to local branch
    git add .
    # check
    git status
    # commit changes
    git commit -m "A message about changes should go here"
    # push changes to remote branch
    git push
    ```

10. Pull from main branch regularly when working on your development branch

    ```bash
    git status # make sure on persaonl dev branch
    # check for updates to main branch
    git fetch origin main
    # pull updates from main into dev branch
    git pull origin main
    git status
    # push local branch updates to remote branch
    git push -u origin main-S # CHANGE 'S' to your initial!
    git status
    # have now merged updates from main branch into personal development branch
    # does not modify/update main branch in any way
    ```

## Merge branch back into main: 

11. Merge development branch back into main 

    ```bash
    # pull updates from main into branch (#10)
    # check updates with dev server and web server (#8)
    # push local branch updates to remote branch (#9)
    # go to github repo branches page: https://github.com/aVISN/CS425_F21/branches
    # click New pull request button for your branch, follow prompts, will check if any merge conflicts, finish merge if not. 
    ```

## Check for errors!

12. Check that merged updates to main did not break site

    ```bash
    # checkout the main branch
    git checkout main
    # get updates
    git fetch origin main
    # pull updates
    git pull origin main
    git status

    # check updates with dev server and web server (#8)
    ```

---
---

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

