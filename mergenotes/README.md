# This directory for notes regarding branch merges, issues from merges, bug fixes. 

## Add file descriptions here: 

*(once resolved, add notes and archive issues by # so that this doc is live issues only.
 keep number, name, and add comment that is resolved in this doc, 
 but move description of issue to new file named by issue number and resolution date, 
 such as 1_11.26.21.md once resolved)* 

---

## 1. commit merged into main from main-D: 
    11/25/21 "got login first and home to go to dashboard (new base) #6"

### files changed: 3
- /srv/apps/visn/pages/temples/base.html
- /srv/apps/visn/pages/temples/dashboard.html
- /srv/apps/visn/pages/urls.py

### issues: 
1. site no longer being served with nginx/uwsgi at localhost (only accessible with django dev server at localhost:8000)
2. login form inaccessible, no longer signifies login success or redirects to custom output based on user 
3. logout functionality removed
4. errors accessing .css resources
---

- nginx issue: when attempting to access site at localhost with web browser, fails, reports error: 
 	```
	NoReverseMatch at /
	Reverse for 'dashboard' not found. 'dashboard' is not a valid view function or pattern name.
	Request Method: 	GET
	Request URL: 	http://localhost/

	Error during template rendering
	In template /srv/apps/visn/pages/templates/base.html, error at line 18
	18 	  <a href="{% url 'dashboard' %}">Home</a> | <a href="{% url 'about' %}">About</a>
	```
	- can also see issue by checking nginx logs:
	```	
	cat /var/log/nginx/access.log # reports 500 response to get request at localhost: 
	127.0.0.1 - - [26/Nov/2021:06:38:45 -0800] "GET / HTTP/1.1" 500 118664 "-" "Mozilla/5.0...

	# same error at 500 response at localhost/login, localhost/register, localhost/about
	```
	- get for localhost/dashboard returns a 404 in browser and shows the urls that Django attempted to use: 
	```
	Page not found (404)
	Request Method: 	GET
	Request URL: 	http://localhost/dashboard

	Using the URLconf defined in visn.urls, Django tried these URL patterns, in this order:

    		admin/
    		[name='home']
    		login/ [name='login']
    		logout/ [name='logout']
    		password_change/ [name='password_change']
    		password_change/done/ [name='password_change_done']
    		password_reset/ [name='password_reset']
    		password_reset/done/ [name='password_reset_done']
    		reset/<uidb64>/<token>/ [name='password_reset_confirm']
    		reset/done/ [name='password_reset_complete']
    		about/ [name='about']
    		register/ [name='register']

	The current path, dashboard, didn’t match any of these.
	```
---
Since can't interact with site with nginx, use Django's dev server: 
```
cd /srv/apps
source venv/bin/activate
cd visn
./manage.py runserver

# navigate to localhost:8000 in web brower
```
---
- using dev server: issues with site navigation, accessing .css resources, no longer indicates successful login, no longer allows user log out, no longer customizes ouput based on user
################################################################################
	```
	page at localhost:8000 is titled "Login" and has a button to "Log in" 
        but is not the login form page, does have link to register
	can see at same time in output from dev server:
        that although the get for '/' has a 200 (OK) response, 
	    there is also a 404 (page not found or file not found error message: 
        indicates that the browser was able to communicate the server, 
        but the server could not find what was requested) response for a
        GET /static/home-style.css request
	```
	```
	clicking "Log in" results in a blank page
	can see in output from dev server:
        that the POST method is not allowed and the post request is returning a 405 
        (method not allowed) response
	(can manually navigate to localhost:8000/login and login form page is loaded)
	```
	```
	heading back to localhost:8000, 
    clicking register link does take user to register page at localhost:8000/register
	and using registration form redirects to login page localhost:8000/login if successful
	but using login form now does nothing to indicate successful login 
    nor does it redirect to dashboard, end up back at localhost:8000 where started
	```
	```
	Clicking "Home" link from localhost:8000 loads localhost:8000/dashboard, 
        however no formatting is applied  
	can see in output from dev server: 
        getting same 404 response for GET /static/home-sytle.css request 
        despite GET /dashboard request succeeding
	Clicking "Home" link in dashboard sidebar reloads dashboard page
	```
	```
	No way for users to log out of app any longer, 
    only way back to page with login and registration is to manually change URL 
    in browser from localhost:8000/dashboard to localhost:8000

	Nothing indicates to user any longer if they are logged in or the username 
    (or some other) dynamic data about the user (i.e. that I, Sarah, am logged in 
    and not Bob, who just used my web browser. 	While there is what looks like a 
    placeholder in the dashboard sidebar, Welcome *NAME*, it is static and 
    not dynamically integrating user name (something that was already implemented 
    in previous home page)
	```
	```
	I can see that users are logged in by accessing the admin site, where it tells me 
    who I am authenticated as and offers me chance to login to different account. 
    By logging into admin site, I can then log out. 

	After logging out, sends me from admin site to localhost:8000 page. 
    When click "Home" link, takes to dashboard - i.e. access to dashboard is not being 
    validated by login. The reason for implementing simple welcome message in original 
    home page was to demonstrate how to display particular information to logged in 
    users (and not to non logged in users). 
	```
---
## 2.

---
## 3. 
