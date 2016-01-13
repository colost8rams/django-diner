Django Diner
============

Simple Django application to handle a collection of recipes.


Requirements
------------

`Diner` wants a modern version of Django — something after 1.8 should work fine.
Django download instruction can be found at
<https://www.djangoproject.com/download>, and installation instruction at
<https://docs.djangoproject.com/en/1.9/intro/install/>.


This project also expects `django.contrib.staticfiles` to be properly installed.
Instructions can be found at
<https://docs.djangoproject.com/en/1.9/ref/contrib/staticfiles/>


`Diner` also requires two other Django apps to function properly,
`django-bootstrap-pagination` and `django-crispy-forms`. Installation
instructions can be found here
<https://github.com/jmcclell/django-bootstrap-pagination> and here
<https://github.com/maraujop/django-crispy-forms> respectively.


Installation
------------

Once the above requirements are met, download `diner` using the following
method:


### Checkout from GitHub

Use the following command:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
git clone http://github.com/towen/diner.git
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Configuration
-------------

Since `Diner` is intended as a sample application for training purposes only, I
have included most everything you need to launch the application including media
files, database, and most settings.


### settings.py

One setting you will want to change is the location of where uploaded media
files are stored. In your `settings.py` file, change the setting `MEDIA_ROOT`
near the bottom of the file to *your* absolute filesystem path of the media
directory inside the diner project.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Example:
    MEDIA_ROOT = '/Users/towen/diner/media'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Once you have changed this setting, launch the Django development server by
invoking the command `python manage.py runserver` within the `diner` project
directory. Your app should now be running at
[http://127.0.0.1:8000/](<http://127.0.0.1:8000/>)


One last thing, the username and password for the app are as follows:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Username: admin
Password: dineradmin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Thanks
------

If you have any questions please feel free to contact me at
[terry@iknowmac.com](<mailto:terry@iknowmac.com>).
