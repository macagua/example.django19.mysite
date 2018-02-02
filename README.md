# django19_mysite

My practices about [Django 1.9 Project tutorial](https://docs.djangoproject.com/en/1.9/intro/) and [Django Rest Framework 3.6.4](http://www.django-rest-framework.org/#tutorial).

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
>>> from myapp.models.music_band import Person, Group, Membership

>>> axl = Person.objects.create(name="Axl Rose")
>>> slash = Person.objects.create(name="Slash")
>>> duff = Person.objects.create(name="Duff McKagan")
>>> izzy = Person.objects.create(name="Izzy Stradlin")
>>> steven = Person.objects.create(name="Steven Adler")

>>> guns_and_roses = Group.objects.create(name="Guns N' Roses")
>>> velvet_revolver = Group.objects.create(name="Velvet Revolver")

>>> scott = Person.objects.create(name="Scott Weiland")
>>> dave = Person.objects.create(name="Dave Kushner")
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
>>> m6 = Membership(person=slash, group=velvet_revolver, date_joined=date(2002, 1, 22), invite_reason="Wanted to form a new band...", actived=True)
>>> m6.save()
>>> m7 = Membership(person=scott, group=velvet_revolver, date_joined=date(2002, 1, 22), invite_reason="Wanted to form a new band...", actived=True)
>>> m7.save()
>>> m8 = Membership(person=dave, group=velvet_revolver, date_joined=date(2002, 1, 22), invite_reason="Wanted to form a new band...", actived=True)
>>> m8.save()
>>> m9 = Membership(person=matt, group=velvet_revolver, date_joined=date(2002, 1, 22), invite_reason="Wanted to form a new band...", actived=True)
>>> m9.save()
>>> m10 = Membership(person=duff, group=velvet_revolver, date_joined=date(1985, 3, 16), invite_reason="Wanted to form a new band...", actived=True)
>>> m10.save()

>>> Membership.objects.all()
[<Membership: Member: True from 1985-03-16>, <Membership: Member: True from 1985-03-16>, <Membership: Member: True from 1985-03-16>, <Membership: Member: True from 1985-03-16>, <Membership: Member: True from 1985-03-16>, <Membership: Member: True from 2002-01-22>, <Membership: Member: True from 2002-01-22>, <Membership: Member: True from 2002-01-22>, <Membership: Member: True from 2002-01-22>, <Membership: Member: True from 1985-03-16>]
>>> Person.objects.all()
[<Person: Axl Rose>, <Person: Slash>, <Person: Duff McKagan>, <Person: Izzy Stradlin>, <Person: Steven Adler>, <Person: Scott Weiland>, <Person: Dave Kushner>, <Person: Matt Sorum>]
>>> Group.objects.all()
[<Group: Guns N' Roses>, <Group: Velvet Revolver>]

>>> axl = Person.objects.get(id=1)
>>> axl
<Person: Axl Rose>

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
>>> slash.group_set.all()
[<Group: Guns N' Roses>, <Group: Velvet Revolver>]
>>> guns_and_roses.members.all()
[<Person: Axl Rose>, <Person: Slash>, <Person: Duff McKagan>, <Person: Izzy Stradlin>, <Person: Steven Adler>]
>>> velvet_revolver.members.all()
[<Person: Slash>, <Person: Scott Weiland>, <Person: Dave Kushner>, <Person: Matt Sorum>, <Person: Duff McKagan>]

>>> Group.objects.filter(members__name__startswith='Slash')
[<Group: Guns N' Roses>, <Group: Velvet Revolver>]
```

# Reference

- [Django 1.9 Project tutorial](https://docs.djangoproject.com/en/1.9/intro/).
- [Django Rest Framework 3.6.4](http://www.django-rest-framework.org/#tutorial).
