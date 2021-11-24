# Repo for VISN online application project

- Repo structure: 
```
/etc/nginx = NGINX config files
/etc/uwsgi = uWSGI config files
/etc/systemd = uWSGI service

/var/www/html = NGINX html files

/srv/apps = VirtualEnv and Django project files

/root = git setup notes
/.gitignore = system wide ignore config to select directories for repo
```


# Projct setup notes: 

## 1. Use VirtualBox* to create a Debian 11 VM (with a desktop) 

- login to desktop as root, open a terminal:
```bash
apt update
# will need these later
apt install vim curl tree
```

## 2. See /etc/nginx/README.md for basic NGINX install and setup walkthrough

## 3. See /srv/apps/README.md for VirtualEnv and Django project setup walkthrough

## 4. See /root/README.md for git and github setup walkthrough and git notes

## 5. See /etc/uwsgi/README.md for uWSGI and NGINX configuration to serve django project

## 6. See /root/hello_github/README.md for walkthrough on setting up personal development branch
      NOTE: currently on main-S branch, not main branch! 
      View on github by selecting main-S branch from drop down button or use address:
      github.com/aVISN/CS425_F21/tree/main-S/root/hello_github
---


### *VirtualBox setup details:

- ENABLE CLIBOARD:
```bash
in VM menu: Devices > Shared Clipboard > Bidirectional
```

- FIX RESOLUTION:
```bash
desktop:  
	click Devices (in VM window menu) > Insert Guest Additions CD Image.
	Mount the CD-ROM with the command mount /dev/cdrom /media/cdrom.
	Change into the mounted directory with the command cd /media/cdrom.
	Install the necessary dependencies with the command apt install -y dkms build-essential linux-headers-$(uname -r).
	Install the Guest Additions package with the command ./VBoxLinuxAdditions.run --nox11
	Allow the installation to complete, reboot
	login to desktop, click View (in VM window menu) > Auto-Resize Guest Display (twice)
```
```bash
for ttys: (if you only use desktop, dont need this): 
	Reboot your system into GRUB menu. Press c key to enter GRUB’s command line. 
	grub> set pager=1
	grub> vbeinfo
	note resolution desired, enter the normal command to continue with normal server boot
	login as root, apt install vim 
	edit /etc/default/grub to include the following settings:
	GRUB_CMDLINE_LINUX_DEFAULT="vga=792" (==1024x768, search for grub vga values, not all in vbeinfo supported)
    restart
```


