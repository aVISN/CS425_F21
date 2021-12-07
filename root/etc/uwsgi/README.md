# Nginx can't talk directly to Django, needs a Web Server Gateway Interface
# uWSGI is the WSGI implmentation we are using

# Dependencies
```bash
apt install uwsgi uwsgi-plugin-python3
systemctl stop uwsgi
systemctl disable uwsgi
```

# Create uWSGI configuration file: 
```bash
/etc/uwsgi/apps-available/visn.ini

# create simlink in apps-enabled: 
ln -s /etc/uwsgi/apps-available/visn.ini /etc/uwsgi/apps-enabled/visn.ini
```

# Update NGINX configution file: 
```bash
# see:
/etc/nginx/sites-available/default
```

# Create systemd service to automatically start site:
```bash
# see: 
/etc/systemd/system/visn-uwsgi.service

# enable and start service: 
# (must enable for service to autostart at reboot)
systemctl enable uwsgi
systemctl start service
```

# Update permissions for database: 
```bash
# need to change owner of database and project for nginx to use
chown www-data /srv/apps/visn/db.sqlite3
chown www-data /srv/apps/visn

# should now be able to interact with site in browser at localhost
```
