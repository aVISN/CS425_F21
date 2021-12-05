# notes on changes made in css-S branch due to issues with css files in main: 

See message from Daniel above, css style sheets for individual pages should go into a styles block in the page's html page template: 
```
{% block styles %} 
  <link rel="stylesheet" href="{%static 'css/page1.css' %}
{% endblock %}
```
By putting 
```
    <link href="{% static 'css/chat.css' %}" rel="stylesheet"/>
    <link href="{% static 'css/all.css' %}" rel="stylesheet"/>
```
into base.html, chat.css is being called by all pages (as we can see in the output of the development server):
```
(venv) root@visn:/srv/apps/visn# ./manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
December 05, 2021 - 12:22:27
Django version 3.2.9, using settings 'visn.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[05/Dec/2021 12:22:44] "GET / HTTP/1.1" 200 2763
[05/Dec/2021 12:22:46] "GET /static/css/home-style.css HTTP/1.1" 304 0
[05/Dec/2021 12:22:46] "GET /static/css/all.css HTTP/1.1" 200 73620
[05/Dec/2021 12:22:46] "GET /static/css/chat.css HTTP/1.1" 200 1495

[05/Dec/2021 12:23:15] "GET /register/ HTTP/1.1" 200 3622
[05/Dec/2021 12:23:15] "GET /static/css/home-style.css HTTP/1.1" 304 0
[05/Dec/2021 12:23:15] "GET /static/css/all.css HTTP/1.1" 304 0
[05/Dec/2021 12:23:15] "GET /static/css/chat.css HTTP/1.1" 304 0

[05/Dec/2021 12:23:26] "GET /dashboard/ HTTP/1.1" 200 6687
[05/Dec/2021 12:23:26] "GET /static/css/home-style.css HTTP/1.1" 304 0
[05/Dec/2021 12:23:26] "GET /static/css/chat.css HTTP/1.1" 304 0
[05/Dec/2021 12:23:26] "GET /static/css/all.css HTTP/1.1" 304 0
[05/Dec/2021 12:23:26] "GET /static/css/dashboard.css HTTP/1.1" 304 0
[05/Dec/2021 12:23:26] "GET /static/pages/Logo_Rev2.png HTTP/1.1" 304 0

[05/Dec/2021 12:23:36] "GET /files/ HTTP/1.1" 200 4791
[05/Dec/2021 12:23:36] "GET /static/css/home-style.css HTTP/1.1" 304 0
[05/Dec/2021 12:23:36] "GET /static/css/chat.css HTTP/1.1" 304 0
[05/Dec/2021 12:23:36] "GET /static/css/all.css HTTP/1.1" 304 0
[05/Dec/2021 12:23:36] "GET /static/pages/Logo_Rev2.png HTTP/1.1" 304 0

[05/Dec/2021 12:24:25] "GET /files/upload/ HTTP/1.1" 200 3925
[05/Dec/2021 12:24:25] "GET /static/css/home-style.css HTTP/1.1" 304 0
[05/Dec/2021 12:24:25] "GET /static/css/chat.css HTTP/1.1" 304 0
[05/Dec/2021 12:24:25] "GET /static/css/all.css HTTP/1.1" 304 0
[05/Dec/2021 12:24:25] "GET /static/pages/Logo_Rev2.png HTTP/1.1" 304 0

[05/Dec/2021 12:23:41] "GET /projects/ HTTP/1.1" 200 3213
[05/Dec/2021 12:23:41] "GET /static/css/home-style.css HTTP/1.1" 304 0
[05/Dec/2021 12:23:41] "GET /static/css/chat.css HTTP/1.1" 304 0
[05/Dec/2021 12:23:41] "GET /static/css/all.css HTTP/1.1" 304 0
[05/Dec/2021 12:23:41] "GET /static/pages/Logo_Rev2.png HTTP/1.1" 304 0
```
When, by it's name I assume it should only be applied to the chat page. 

Thus, as Daniel noted in previous comments, it should go into a style block on the chat.html page (the styleblock is shown right below where you added the css references in base.html:   
```
    {% block styles %}
    <!-- block of style links for each page -->
    {% endblock styles%}
```
just like the content block that is inherited by pages that extend base.html, the style block is then used in each page like so: (in dashboard.html):
```
{% block styles %}
   <link rel="stylesheet" href="{% static 'css/dashboard.css' %}">
{% endblock styles %}
```


# 1. fix chat.css being called by all pages: 

removed from base.html: 
```
    <link href="{% static 'css/chat.css' %}" rel="stylesheet"/>
```
added to chat.html: 
```
{% load static %}

{% block styles %}
   <link rel="stylesheet" href="{% static 'css/chat.css' %}">
{% endblock styles %}
```
That fixed the issue of chat.css being called by all pages (tested with dev server). 


In addition, when the chat page is loaded, in the terminal, 404 errors are reported by the development server for the webfonts used by chat.html even though chat.css and all.css are being successfully returned; and in the web browser, the button called in the search wrapper and the button called in the Comments or email section fail to load icons within the buttons: 

these are the lines that are failing: 
```
<i class="fas fa-search"></i>
<i class="fa fa-paper-plane" aria-hidden="true"></i>
```
this is the result: 
###IMG
and as seen here in the dev server output: 
```
[05/Dec/2021 12:22:44] "GET / HTTP/1.1" 200 2763
[05/Dec/2021 12:22:46] "GET /static/css/home-style.css HTTP/1.1" 304 0
[05/Dec/2021 12:22:46] "GET /static/css/all.css HTTP/1.1" 200 73620
[05/Dec/2021 12:22:46] "GET /static/css/chat.css HTTP/1.1" 200 1495

[05/Dec/2021 12:23:46] "GET /chat/ HTTP/1.1" 200 7481
[05/Dec/2021 12:23:46] "GET /static/webfonts/fa-solid-900.woff2 HTTP/1.1" 404 1840
[05/Dec/2021 12:23:46] "GET /static/webfonts/fa-solid-900.woff HTTP/1.1" 404 1837
[05/Dec/2021 12:23:46] "GET /static/webfonts/fa-solid-900.ttf HTTP/1.1" 404 1834
[05/Dec/2021 12:23:56] "GET /chat/ HTTP/1.1" 200 7481
[05/Dec/2021 12:23:56] "GET /static/css/home-style.css HTTP/1.1" 304 0
[05/Dec/2021 12:23:56] "GET /static/css/chat.css HTTP/1.1" 304 0
[05/Dec/2021 12:23:56] "GET /static/css/all.css HTTP/1.1" 304 0
[05/Dec/2021 12:23:56] "GET /static/pages/Logo_Rev2.png HTTP/1.1" 304 0
[05/Dec/2021 12:23:56] "GET /static/webfonts/fa-solid-900.woff2 HTTP/1.1" 404 1840
[05/Dec/2021 12:23:56] "GET /static/webfonts/fa-solid-900.woff HTTP/1.1" 404 1837
[05/Dec/2021 12:23:56] "GET /static/webfonts/fa-solid-900.ttf HTTP/1.1" 404 1834
```
This is because the /webfonts directory that your all.css relies on does not exist:
```
src: url("../webfonts/fa-....")
```

Rather than uploading and locally hosting the entire font awesome library, I am going to add the cdn link to our base.html file. (See article on benefits of using cdn instead of local hosting: https://www.belugacdn.com/bootstrap-local-vs-cdn/ )

# 2. fix 404 errors for button icons in chat.html: 

Added cdn to base.html and removed link to all.css from base.html, fontawesome can now be used by all pages that extend base.html: 
```
    <!-- Font Awesome CSS -->
    <!-- replaced local all.css with cdn, see: https://fontawesome.com/account/cdn 
	    cdn still uses all.css, see: https://github.com/FortAwesome/Font-Awesome/blob/master/css/all.css 
	    to override something from all.css now, add class to either base.css (for all pages) 
	    or a particular page's .css file such as chat.css. -->
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.4/css/all.css" integrity="sha384-DyZ88mC6Up2uqS4h/KRgHuoeGwBcD4Ng9SiP4dIRy0EXTlnuz47vAwmeGwVChigm" crossorigin="anonymous">
```

Also note that the fa prefix was depreciated in fontawesome version 5. In Version 5, the solid, regular, light, and duotone styles were released for every icon in Font Awesome. It also separated out brand icons into their own style/category for easier use. The free library gives us access to solid and brand only, so previous uses of fa should be replaced with fas and the brand styles are now prefixed with fab. 

Updated chat.html to use new prefix for fa-paper-plane: 
from: 
```
<i class="fa fa-paper-plane" aria-hidden="true"></i>
```
to:   
```
<i class="fas fa-paper-plane" aria-hidden="true"></i>
```

# 3. removed all.css, as noted above, to customize particular fontawesome css classes, add changes to base.css (renaming home-style.css base.css so that it is easy to see it is the entire site's css base)

# 4. There was an old home-style.css in pages/static/pages/ (the one in pages/static/css had more recent updates). Removed the old one to reduce confusion.

# 5. Renamed the current home-style.css to base.css so that it is more obvious that it is for the entire site, not just old "home" page. 

# 6. Finally, while everything is now working in the development server, when I check localhost (i.e. using nginx), although my urls are returning 200 codes, the static file requests are all returning 404 codes:
```

::1 - - [05/Dec/2021:10:19:33 -0800] "GET /favicon.ico HTTP/1.1" 499 0 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
127.0.0.1 - - [05/Dec/2021:10:19:38 -0800] "GET /dashboard/ HTTP/1.1" 200 2129 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
127.0.0.1 - - [05/Dec/2021:10:19:38 -0800] "GET /static/css/base.css HTTP/1.1" 404 125 "http://localhost/dashboard/" "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
127.0.0.1 - - [05/Dec/2021:10:19:38 -0800] "GET /static/css/dashboard.css HTTP/1.1" 404 125 "http://localhost/dashboard/" "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
127.0.0.1 - - [05/Dec/2021:10:19:38 -0800] "GET /static/pages/Logo_Rev2.png HTTP/1.1" 404 125 "http://localhost/dashboard/" "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
127.0.0.1 - - [05/Dec/2021:10:19:38 -0800] "GET /static/pages/Logo_Rev2.png HTTP/1.1" 404 125 "http://localhost/dashboard/" "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
127.0.0.1 - - [05/Dec/2021:10:19:44 -0800] "GET /files/ HTTP/1.1" 200 1986 "http://localhost/dashboard/" "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
127.0.0.1 - - [05/Dec/2021:10:19:44 -0800] "GET /static/css/base.css HTTP/1.1" 404 125 "http://localhost/files/" "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
127.0.0.1 - - [05/Dec/2021:10:19:44 -0800] "GET /static/pages/Logo_Rev2.png HTTP/1.1" 404 125 "http://localhost/files/" "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
127.0.0.1 - - [05/Dec/2021:10:19:44 -0800] "GET /static/pages/Logo_Rev2.png HTTP/1.1" 404 125 "http://localhost/files/" "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
127.0.0.1 - - [05/Dec/2021:10:19:45 -0800] "GET /chat/ HTTP/1.1" 200 2067 "http://localhost/files/" "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
127.0.0.1 - - [05/Dec/2021:10:19:45 -0800] "GET /static/css/base.css HTTP/1.1" 404 125 "http://localhost/chat/" "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
127.0.0.1 - - [05/Dec/2021:10:19:45 -0800] "GET /static/pages/Logo_Rev2.png HTTP/1.1" 404 125 "http://localhost/chat/" "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
127.0.0.1 - - [05/Dec/2021:10:19:45 -0800] "GET /static/css/chat.css HTTP/1.1" 404 125 "http://localhost/chat/" "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
127.0.0.1 - - [05/Dec/2021:10:19:45 -0800] "GET /static/pages/Logo_Rev2.png HTTP/1.1" 404 125 "http://localhost/chat/" "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
```

This is because ./manage.py collectstatic wasn't run after adding static files. The collectstatic script collects static files for nginx to serve directly. 

Let's run the script, restart nginx and uwsgi and try again: 
```
./manage.py collectstatic
systemctl restart nginx
systemctl restart uwsgi
```
Et voila! We have a working site again!
