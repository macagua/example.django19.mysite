# django19_mysite
My practices about Django 1.9 Project tutorial https://docs.djangoproject.com/en/1.9/intro/

## Installation

This Django Web app need a lot of Python extras packages, please execute the following command:

```bash
$ pip install -r requirements.txt --timeout 120
```

### Build the Django Web app DB

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```
### Create Django Admin User

This Django Web app need a to create a Django Admin User, for access and manager the Admin interface, please execute the following command:

**Tip:** for this local installation use the user as **admin** and password as **admin**.

```bash
$ python manage.py createsuperuser
Username (leave blank to use 'user'): admin
Email address: your-user@mail.com
Password: 
Password (again): 
Superuser created successfully.
```

## Run the Django Web app

You need to run the Django server, please execute the following command::

```bash
$ python manage.py runserver
```

- Open your web browser with the following URL: [http://0.0.0.0:8000/](http://0.0.0.0:8000/) and see the Django Web app.

- Open your web browser with the following URL: [http://0.0.0.0:8000/admin/](http://0.0.0.0:8000/admin/) and see the Django Admin Interface, use the user **admin** and password **admin**.

# Reference

- [Django 1.9 Project tutorial](https://docs.djangoproject.com/en/1.9/intro/).
