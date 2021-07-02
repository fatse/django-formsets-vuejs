# Dynamic forms with Django and Vue.js 

This is an initial proof of concept of how to build dynamic forms with Django and Vue.js 

Content:
1. [Overview](#1-overview)
2. [Set up the working environment](#2-set-up-the-working-environment)
3. [Run Django server](#3-run-django-server)


## 1. Overview

In this web application users can manage an author and their books by adding new books or removing books, or updating the info for the existing books. 

Here's a demo of this web app:  https://fatse.pythonanywhere.com/

## 2. Set up the working environment

2.1 Clone the project repository in your machine and change the current working directory to that of the cloned project as follows:

```commandline
git clone https://github.com/fatse/django-formsets-vuejs.git
cd django-formsets-vuejs
```

2.2 Install dependencies into an isolated environment:

```commandline
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## 3. Run Django server


From your terminal run this command to start a local web server: 

```commandline
python manage.py runserver
```

And in your terminal you will see an output similar to the one below:

```commandline
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
July 02, 2021 - 21:48:12
Django version 2.2.24, using settings 'django_vuejs.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

You can copy the url `http://127.0.0.1:8000/` from the output and paste it directly to your browser's search bar.

Alternatively, you can click at the link `http://127.0.0.1:8000/` from the output while pressing the `Command ⌘` key, and it
will open a new browser tab for the web application.
