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

You need to run the Django server, please execute the following command:

```bash
$ python manage.py runserver
```

- Open your web browser with the following URL: [http://0.0.0.0:8000/](http://0.0.0.0:8000/) and see the Django Web app.

- Open your web browser with the following URL: [http://0.0.0.0:8000/admin/](http://0.0.0.0:8000/admin/) and see the Django Admin Interface, use the user **admin** and password **admin**.

## Django ORM Practices

For make some practices the Django ORM, please execute the following command:

```bash
$ python manage.py shell
Python 2.7.13 (default, Nov 24 2017, 17:33:09) 
[GCC 6.3.0 20170516] on linux2
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> 
```

At Python Interactive Console, please execute the following command:

```python
>>> from myapp.models import Person, Group, Membership

>>> axl = Person.objects.create(name="Axel Rose")
>>> slash = Person.objects.create(name="Slash")
>>> duff = Person.objects.create(name="Duff McKagan")
>>> izzy = Person.objects.create(name="Izzy Stradlin")
>>> steven = Person.objects.create(name="Steven Adler")

>>> guns_and_roses = Group.objects.create(name="Guns N' Roses")
>>> matt = Person.objects.create(name="Matt Sorum")

>>> from datetime import date

>>> m1 = Membership(person=axl, group=guns_and_roses, date_joined=date(1985, 3, 16), invite_reason="Wanted to form a band..", actived=True)
>>> m1.save()
>>> m2 = Membership(person=slash, group=guns_and_roses, date_joined=date(1985, 3, 16), invite_reason="Wanted to form a band..", actived=True)
>>> m2.save()
>>> m3 = Membership(person=duff, group=guns_and_roses, date_joined=date(1985, 3, 16), invite_reason="Wanted to form a band..", actived=True)
>>> m3.save()
>>> m4 = Membership(person=izzy, group=guns_and_roses, date_joined=date(1985, 3, 16), invite_reason="Wanted to form a band..", actived=True)
>>> m4.save()
>>> m5 = Membership(person=steven, group=guns_and_roses, date_joined=date(1985, 3, 16), invite_reason="Wanted to form a band..", actived=True)
>>> m5.save()

>>> Membership.objects.all()
[<Membership: Member: True from 1985-03-16>, <Membership: Member: True from 1985-03-16>, <Membership: Member: True from 1985-03-16>, <Membership: Member: True from 1985-03-16>, <Membership: Member: True from 1985-03-16>]
>>> Person.objects.all()
[<Person: Axel Rose>, <Person: Slash>, <Person: Duff McKagan>, <Person: Izzy Stradlin>, <Person: Steven Adler>]
>>> Group.objects.all()
[<Group: Guns N' Roses>]
>>> 

>>> axl = Person.objects.get(id=1)
>>> axl
<Person: Axel Rose>

>>> guns_and_roses = Group.objects.get(id=1)
>>> guns_and_roses
<Group: Guns N' Roses>

>>> axl_membership = Membership.objects.get(group=guns_and_roses, person=axl)
>>> axl_membership
<Membership: Member: True from 1985-03-16>
>>> axl_membership.date_joined
datetime.date(1985, 3, 16)
>>> axl_membership.invite_reason
u'Wanted to form a band..'

>>> axl.group_set.all()
[<Group: Guns N' Roses>]
>>> guns_and_roses.members.all()
[<Person: Axel Rose>, <Person: Slash>, <Person: Duff McKagan>, <Person: Izzy Stradlin>, <Person: Steven Adler>]

>>> Group.objects.filter(members__name__startswith='Sl')
[<Group: Guns N' Roses>]
```

# Reference

- [Django 1.9 Project tutorial](https://docs.djangoproject.com/en/1.9/intro/).
