# This is where NGINX stores configuration files. 


# Basic nginx installation and setup: 

## 1. Install nginx
```
apt install nginx
systemctl status nginx # should be active and running
curl localhost 
# can also see in web browser, put localhost or 127.0.0.1 in address bar
# these are the nginx config files:
cd /etc/nginx && ls --color  
    # main server config file: /etc/nginx/nginx.conf
    # all sites config files: /etc/nginx/sites-available
    # simlinks to available so easy to turn sites on/off: /etc/nginx/sites-enabled
# these are the html files used by nginx
cd /var/www/html && ls
    # index.nginx-debian.html is the default page
```

## 2. Create a simple page at localhost/test in /var/www/html

- lets create a simple page: 
```
vim test.html 
# add text and save:
This is a simple NGINX page.
```

- now we need to add the location to our site config file:
```
cd /etc/nginx/sites-available
vim default
# under the location / {...} block, add the following and save the file: 
	location /test {
		try_files $uri $uri/ $uri.html =404;
	}
```

- now we can check our config file for errors: 
```
nginx -t
```

- and anytime we change a config file we need to reload nginx to serve the new content:
```
systemctl reload nginx
```

- check for new page: 
```
curl localhost/test # or in web browser address bar: localhost/test
```
