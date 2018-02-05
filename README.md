# django19_mysite

My practices about the following tutorials:

- [Django 1.9 Project tutorial](https://docs.djangoproject.com/en/1.9/intro/).
- [Django Rest Framework 3.6.4](http://www.django-rest-framework.org/#tutorial).
- [Introducción a Django Rest Framework](https://axiacore.com/blog/2012/06/introduccion-a-django-rest-framework/).
- [Levi Velázquez · Crear un API REST con Django Rest Framework - Parte I](http://levipy.com/crear-api-rest-con-django-rest-framework/).
- [Django 1.7 - introducción a Django REST Framework](http://blog.enriqueoriol.com/2015/01/django-1.7-intro-django-rest-framework.html).
- [Django REST Framework: Serializers anidados y ModelViewSet](http://blog.enriqueoriol.com/2015/03/django-rest-framework-serializers.html).

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
$ python manage.py createsuperuser --email admin@mail.com --username admin
Password: 
Password (again): 
Superuser created successfully.
```

## Run the Django Web app

You need to run the Django server, please execute the following command:

```bash
$ python manage.py runserver
```

- Open your web browser with the following URL: [http://localhost:8000/](http://localhost:8000/) and see the Django Web app.

- Open your web browser with the following URL: [http://localhost:8000/admin/](http://localhost:8000/admin/) and see the Django Admin Interface, use the user **admin** and password **admin**.

### Band App

For add data for *Band* App, please access to the following URL: [http://localhost:8000/admin/band/](http://localhost:8000/admin/band/)

### My Application App

For add data for *My Application* App, please access to the following URL: [http://localhost:8000/admin/myapp/](http://localhost:8000/admin/myapp/)

### Points Of Sale App

For add data for *Points Of Sale* App, please access to the following URL: [http://localhost:8000/admin/pos/](http://localhost:8000/admin/pos/)

### Polls App

For add data for *Polls* App, please access to the following URL: [http://localhost:8000/admin/polls/](http://localhost:8000/admin/polls/)

### Survey App

For add data for *Survey* App, please access to the following URL: [http://localhost:8000/admin/survey/](http://localhost:8000/admin/survey/)

### Webflix App

For add data for *Webflix* App, please access to the following URL: [http://localhost:8000/admin/webflix/](http://localhost:8000/admin/webflix/)

### Testing the API

You have many APIs Rest for testing, now access to the APIs, both from the command-line, using tools like **curl**, please execute the following command:

#### Points Of Sale list endpoint

For testing the **Points Of Sale list** API Rest, please execute the following command:

```bash
$ curl -H 'Accept: application/json; indent=4' -u admin:password123 http://localhost:8000/pos/list/
[
    {
        "id": 2,
        "name": "Restaurante Tinjaca",
        "address": "Av. 3, Hotel Tinjaca, frente al CC Gran Mundo, Centro, Merida, Venezuela",
        "brand": "Hotel Tinjaca",
        "longitude": "8.5897200",
        "latitude": "-71.1561100",
        "options": "N/P",
        "userprofile": [
            "http://localhost:8000/mysite/userprofiles/2/"
        ],
        "message": "Registrado",
        "actived": true
    },
    {
        "id": 1,
        "name": "Churros Ezq. Dorzay",
        "address": "Av. 4, Ezq. Dorzay, Centro, Merida, Venezuela",
        "brand": "Dorzay",
        "longitude": "8.5897200",
        "latitude": "-71.1561100",
        "options": "N/P",
        "userprofile": [
            "http://localhost:8000/mysite/userprofiles/1/"
        ],
        "message": "Registrado",
        "actived": true
    }
]
```

#### Points Of Sale detail endpoint

For testing the **Points Of Sale detail** API Rest, please execute the following command:

```bash
$ curl -H 'Accept: application/json; indent=4' -u admin:password123 http:/localhost:8000/pos/list/1/
{
    "id": 1,
    "name": "Churros Ezq. Dorzay",
    "address": "Av. 4, Ezq. Dorzay, Centro, Merida, Venezuela",
    "brand": "Dorzay",
    "longitude": "8.5897200",
    "latitude": "-71.1561100",
    "options": "N/P",
    "userprofile": [
        "http://localhost:8000/mysite/userprofiles/1/"
    ],
    "message": "Registrado",
    "actived": true
}
```

You can also consume this API endpoint using a web client demo based on Javascrit by accessing the following URL: [http://localhost:8000/pos/web-client/](http://localhost:8000/pos/web-client/).

#### User Profiles list endpoint

For testing the **User Profiles list** API Rest, please execute the following command:

```bash
$ curl -H 'Accept: application/json; indent=4' -u admin:password123 http://localhost:8000/mysite/userprofiles/
[
    {
        "id": 1,
        "user": "admin",
        "photo": "http://localhost:8000/mysite/userprofiles/myapp/static/images/avatars/patacon.jpg",
        "website": "http://localhost:8000/admin/",
        "bio": "Website Aministrator",
        "phone": "+58 0987654321",
        "city": "Maracaibo",
        "country": "Venezuela",
        "organization": "My Company"
    },
    {
        "id": 2,
        "user": "leonardo",
        "photo": "http://localhost:8000/mysite/userprofiles/myapp/static/images/avatars/yo.png",
        "website": "https://macagua.github.io/",
        "bio": "Leonardo José Caballero Garcia is Technical Director at Covantec R.L. firm. He has over 15 years experience in the area of Information Technology of which 12 years are unique in free and open-source software.",
        "phone": "+58 1234567890",
        "city": "Rubio",
        "country": "Venezuela",
        "organization": "Plone Venezuela"
    }
]
```

#### User Profiles detail endpoint

For testing the **User Profiles detail** API Rest, please execute the following command:

```bash
$ curl -H 'Accept: application/json; indent=4' -u admin:password123 http:/localhost:8000/mysite/userprofiles/1/
{
    "id": 1,
    "user": "admin",
    "photo": "http://localhost:8000/mysite/userprofiles/1/myapp/static/images/avatars/patacon.jpg",
    "website": "http://localhost:8000/admin/",
    "bio": "Website Aministrator",
    "phone": "+58 0987654321",
    "city": "Maracaibo",
    "country": "Venezuela",
    "organization": "My Company"
}
```

#### Users list endpoint

For testing the **users list** API Rest, please execute the following command:

```bash
$ curl -H 'Accept: application/json; indent=4' -u admin:password123 http://localhost:8000/mysite/users/
[
    {
        "url": "http://localhost:8000/mysite/users/2/",
        "username": "leonardo",
        "email": "leonardo@mail.com",
        "is_staff": true
    },
    {
        "url": "http://localhost:8000/mysite/users/1/",
        "username": "admin",
        "email": "admin@mail.com",
        "is_staff": true
    }
]
```

#### Users detail endpoint

For testing the **users detail** API Rest, please execute the following command:

```bash
$ curl -H 'Accept: application/json; indent=4' -u admin:password123 http:/localhost:8000/mysite/users/1/
{
    "url": "http://localhost:8000/mysite/users/1/",
    "username": "admin",
    "email": "admin@mail.com",
    "is_staff": true
}
```

#### Questions list endpoint

For testing the **questions list** API Rest, please execute the following command:

```bash
$ curl -H 'Accept: application/json; indent=4' -u admin:password123 http://localhost:8000/polls/questions/
[
    {
        "id": 2,
        "question_text": "Django is Cool?",
        "pub_date": "2018-02-03T15:17:16Z"
    },
    {
        "id": 1,
        "question_text": "Plone rocks?",
        "pub_date": "2018-02-04T15:16:52Z"
    }
]
```

#### Questions detail endpoint

For testing the **questions detail** API Rest, please execute the following command:

```bash
$ curl -H 'Accept: application/json; indent=4' -u admin:password123 http:/localhost:8000/polls/questions/1/
{
    "id": 1,
    "question_text": "Plone rocks?",
    "pub_date": "2018-02-04T15:16:52Z"
}
```

#### Choices list endpoint

For testing the **choices list** API Rest, please execute the following command:

```bash
$ curl -H 'Accept: application/json; indent=4' -u admin:password123 http://localhost:8000/polls/choices/
[
    {
        "id": 5,
        "choice_text": "Nothing",
        "votes": 0,
        "question": 1
    },
    {
        "id": 4,
        "choice_text": "Very little",
        "votes": 0,
        "question": 1
    },
    {
        "id": 3,
        "choice_text": "Little bit",
        "votes": 0,
        "question": 1
    },
    {
        "id": 2,
        "choice_text": "A lot",
        "votes": 0,
        "question": 1
    },
    {
        "id": 1,
        "choice_text": "Too",
        "votes": 0,
        "question": 1
    }
]
```

#### Choices detail endpoint

For testing the **choices detail** API Rest, please execute the following command:

```bash
$ curl -H 'Accept: application/json; indent=4' -u admin:password123 http:/localhost:8000/polls/choices/1/
{
    "id": 1,
    "choice_text": "Too",
    "votes": 0,
    "question": 1
}
```

#### Survey list endpoint

For testing the **survey list** API Rest, please execute the following command:

```bash
$ curl -H 'Accept: application/json; indent=4' -u admin:password123 http:/localhost:8000/survey/list/
[
    {
        "id": 1,
        "owner": "Leonardo",
        "title": "Half time of Super Bowl 2018",
        "question": "What about the Half time of Super Bowl 2018?",
        "active": true,
        "created": "2018-02-05T04:06:00.667815Z",
        "updated": "2018-02-05T04:06:00.667912Z"
    },
    {
        "id": 2,
        "owner": "Macagua",
        "title": "About Django",
        "question": "What do you thing about Django?",
        "active": true,
        "created": "2018-02-05T04:25:36.718465Z",
        "updated": "2018-02-05T04:25:36.718561Z"
    }
]
```

#### Survey detail endpoint

For testing the **survey detail** API Rest, please execute the following command:

```bash
$ curl -H 'Accept: application/json; indent=4' -u admin:password123 http://localhost:8000/survey/detail/1/
{
    "id": 1,
    "owner": "Leonardo",
    "title": "Half time of Super Bowl 2018",
    "question": "What about the Half time of Super Bowl 2018?",
    "active": true,
    "created": "2018-02-05T04:06:00.667815Z",
    "updated": "2018-02-05T04:06:00.667912Z"
}
```

#### Survey delete endpoint

For testing the **survey delete** API Rest, please execute the following command:

```bash
$ curl -i -X DELETE -H 'Accept: application/json; indent=4' -u admin:password123 http://localhost:8000/survey/detail/2/
HTTP/1.0 204 No Content
Date: Mon, 05 Feb 2018 06:17:51 GMT
Server: WSGIServer/0.1 Python/2.7.13
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN
Content-Length: 0
Allow: PUT, GET, OPTIONS, DELETE

```

#### Tv Series list endpoint

For testing the **Tv Series list** API Rest, please execute the following command:

```bash
$ curl -H 'Accept: application/json; indent=4' -u admin:password123 http://localhost:8000/webflix/tv-series/list/
[{"id":1,"name":"Game of Thrones","release_date":"2011-04-17","rating":0,"category":"drama"},{"id":2,"name":"Mr. Robot","release_date":"2015-06-24","rating":0,"category":"drama"},{"id":4,"name":"Timeless","release_date":"2016-02-04","rating":3,"category":"fiction"},{"id":5,"name":"Black Mirror","release_date":"2011-12-17","rating":0,"category":"fiction"}]
```

#### Tv Series detail endpoint

For testing the **Tv Series detail** API Rest, please execute the following command:

```bash
$ curl -H 'Accept: application/json; indent=4' -u admin:password123 http://localhost:8000/webflix/tv-series/detail/1/
{"id":1,"name":"Game of Thrones","release_date":"2011-04-17","rating":0,"category":"drama"}
```

#### Tv Series create endpoint

For testing the **Tv Series create** API Rest, please execute the following command:

```bash
$ curl -i -X POST -H 'Accept: application/json; indent=4' -u admin:password123 -d '{"name":"Alf","release_date":"1985-04-17","rating":4,"category":"comedy"}' http://localhost:8000/webflix/tv-series/list/
HTTP/1.0 201 Created
Date: Sun, 04 Feb 2018 23:07:06 GMT
Server: WSGIServer/0.1 Python/2.7.13
X-Frame-Options: SAMEORIGIN
Content-Type: application/json

{"id":4,"name":"Alf","release_date":"1985-04-17","rating":4,"category":"comedy"}
```

#### Tv Series update endpoint

For testing the **Tv Series update** API Rest, please execute the following command:

```bash
$ curl -i -X PUT -H 'Accept: application/json; indent=4' -u admin:password123 -d '{"name":"ALF","release_date":"1990-09-22","rating":4,"category":"comedy"}' http://localhost:8000/webflix/tv-series/detail/4/
HTTP/1.0 200 OK
Date: Sun, 04 Feb 2018 23:08:58 GMT
Server: WSGIServer/0.1 Python/2.7.13
X-Frame-Options: SAMEORIGIN
Content-Type: application/json

{"id":4,"name":"ALF","release_date":"1990-09-22","rating":4,"category":"comedy"}
```

#### Tv Series delete endpoint

For testing the **Tv Series delete** API Rest, please execute the following command:

```bash
$ curl -X "DELETE" -H 'Accept: application/json; indent=4' -u admin:password123 http://localhost:8000/webflix/tv-series/detail/4/
```

#### Posts list endpoint

For testing the **posts list** API Rest, please execute the following command:

```bash
$ curl -H 'Accept: application/json; indent=4' -u admin:password123  http://localhost:8000/myapp/v1/posts/
[
    {
        "id": 1,
        "title": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer egestas sodales congue. Fusce finibus augue at erat malesuada, ut lacinia mi iaculis. Maecenas posuere massa nunc, sed rutrum risus mattis non. Sed purus diam, tincidunt vitae quam et, lobortis gravida massa. Aenean ut lectus tortor. Integer consectetur convallis nulla. Duis sit amet ex sapien. Integer mauris lectus, lacinia sed nulla eget, vulputate posuere nunc. Nunc tempor vitae dui non sagittis.\r\n\r\nAenean interdum, nunc id porttitor efficitur, lacus eros interdum ante, et luctus justo quam ut purus. In sed sem lacus. Sed lacinia ipsum et interdum vestibulum. Curabitur porttitor sapien non dignissim dictum. Sed id ipsum ut nulla efficitur lacinia. Nullam molestie, arcu sed elementum malesuada, nibh lacus ornare tellus, facilisis scelerisque purus odio id erat. Sed porta bibendum tortor eleifend pretium.\r\n\r\nSed eleifend eu leo vitae egestas. Vivamus lobortis tincidunt sapien, vitae hendrerit ipsum pellentesque vel. Aenean risus leo, hendrerit in fringilla nec, iaculis id tellus. Sed posuere lorem vitae eros posuere viverra. Duis convallis egestas viverra. Aenean bibendum in nulla nec pellentesque. Duis vel porta nisi. Nunc accumsan magna at turpis congue, ac venenatis risus dictum. Fusce vel nisl vel lectus pretium interdum porttitor commodo mi.",
        "owner": {
            "id": 2,
            "user": "leonardo",
            "photo": "http://localhost:8000/myapp/v1/posts/myapp/static/images/avatars/yo.png",
            "website": "https://macagua.github.io/",
            "bio": "Leonardo José Caballero Garcia is Technical Director at Covantec R.L. firm. He has over 15 years experience in the area of Information Technology of which 12 years are unique in free and open-source software.",
            "phone": "+58 1234567890",
            "city": "Rubio",
            "country": "Venezuela",
            "organization": "Plone Venezuela"
        },
        "comments": [
            {
                "text": "Look so great!",
                "owner": 1
            },
            {
                "text": "Thanks, it's the idea ;-)",
                "owner": 2
            },
            {
                "text": "Really thanks you for the post!",
                "owner": 1
            }
        ]
    },
    {
        "id": 2,
        "title": "New version for our Website",
        "body": "New version for our Website is cool more faster with zero erros ;-)\r\n\r\nEnjoy it!\r\n\r\nBest\r\n--\r\nThe Webmaster",
        "owner": {
            "id": 1,
            "user": "admin",
            "photo": "http://localhost:8000/myapp/v1/posts/myapp/static/images/avatars/patacon.jpg",
            "website": "http://localhost:8000/admin/",
            "bio": "Website Aministrator",
            "phone": "+58 0987654321",
            "city": "Maracaibo",
            "country": "Venezuela",
            "organization": "My Company"
        },
        "comments": [
            {
                "text": "Thanks you :-)",
                "owner": 2
            },
            {
                "text": "No problem ;-)",
                "owner": 1
            }
        ]
    }
]
```

#### Posts detail endpoint

For testing the **posts detail** API Rest, please execute the following command:

```bash
$ $ curl -H 'Accept: application/json; indent=4' -u admin:password123  http:/localhost:8000/myapp/v1/post/2/
{
    "id": 2,
    "title": "New version for our Website",
    "body": "New version for our Website is cool more faster with zero erros ;-)\r\n\r\nEnjoy it!\r\n\r\nBest\r\n--\r\nThe Webmaster",
    "owner": {
        "id": 1,
        "user": "admin",
        "photo": "http://localhost:8000/myapp/v1/post/4/myapp/static/images/avatars/patacon.jpg",
        "website": "http://localhost:8000/admin/",
        "bio": "Website Aministrator",
        "phone": "+58 0987654321",
        "city": "Maracaibo",
        "country": "Venezuela",
        "organization": "My Company"
    },
    "comments": [
        {
            "text": "Thanks you :-)",
            "owner": 2
        },
        {
            "text": "No problem ;-)",
            "owner": 1
        }
    ]
}
```

#### Posts delete endpoint

For testing the **posts delete** API Rest, please execute the following command:

```bash
$ curl -i -X DELETE -H 'Accept: application/json; indent=4' -u admi:password123 http://localhost:8000/myapp/v1/post/1/
HTTP/1.0 204 No Content
Date: Mon, 05 Feb 2018 08:39:38 GMT
Server: WSGIServer/0.1 Python/2.7.13
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN
Content-Length: 0
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS

```

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
>>> from band.models import Member, Group, Membership

>>> axl = Member.objects.create(name="Axl Rose")
>>> slash = Member.objects.create(name="Slash")
>>> duff = Member.objects.create(name="Duff McKagan")
>>> izzy = Member.objects.create(name="Izzy Stradlin")
>>> steven = Member.objects.create(name="Steven Adler")

>>> guns_and_roses = Group.objects.create(name="Guns N' Roses")
>>> velvet_revolver = Group.objects.create(name="Velvet Revolver")

>>> scott = Member.objects.create(name="Scott Weiland")
>>> dave = Member.objects.create(name="Dave Kushner")
>>> matt = Member.objects.create(name="Matt Sorum")

>>> from datetime import date

>>> m1 = Membership(member=axl, group=guns_and_roses, date_joined=date(1985, 3, 16), invite_reason="Wanted to form a band..", actived=True)
>>> m1.save()
>>> m2 = Membership(member=slash, group=guns_and_roses, date_joined=date(1985, 3, 16), invite_reason="Wanted to form a band..", actived=True)
>>> m2.save()
>>> m3 = Membership(member=duff, group=guns_and_roses, date_joined=date(1985, 3, 16), invite_reason="Wanted to form a band..", actived=True)
>>> m3.save()
>>> m4 = Membership(member=izzy, group=guns_and_roses, date_joined=date(1985, 3, 16), invite_reason="Wanted to form a band..", actived=True)
>>> m4.save()
>>> m5 = Membership(member=steven, group=guns_and_roses, date_joined=date(1985, 3, 16), invite_reason="Wanted to form a band..", actived=True)
>>> m5.save()
>>> m6 = Membership(member=slash, group=velvet_revolver, date_joined=date(2002, 1, 22), invite_reason="Wanted to form a new band...", actived=True)
>>> m6.save()
>>> m7 = Membership(member=scott, group=velvet_revolver, date_joined=date(2002, 1, 22), invite_reason="Wanted to form a new band...", actived=True)
>>> m7.save()
>>> m8 = Membership(member=dave, group=velvet_revolver, date_joined=date(2002, 1, 22), invite_reason="Wanted to form a new band...", actived=True)
>>> m8.save()
>>> m9 = Membership(member=matt, group=velvet_revolver, date_joined=date(2002, 1, 22), invite_reason="Wanted to form a new band...", actived=True)
>>> m9.save()
>>> m10 = Membership(member=duff, group=velvet_revolver, date_joined=date(1985, 3, 16), invite_reason="Wanted to form a new band...", actived=True)
>>> m10.save()

>>> Membership.objects.all()
[<Membership: Member: True from 1985-03-16>, <Membership: Member: True from 1985-03-16>, <Membership: Member: True from 1985-03-16>, <Membership: Member: True from 1985-03-16>, <Membership: Member: True from 1985-03-16>, <Membership: Member: True from 2002-01-22>, <Membership: Member: True from 2002-01-22>, <Membership: Member: True from 2002-01-22>, <Membership: Member: True from 2002-01-22>, <Membership: Member: True from 1985-03-16>]
>>> Member.objects.all()
[<Member: Axl Rose>, <Member: Slash>, <Member: Duff McKagan>, <Member: Izzy Stradlin>, <Member: Steven Adler>, <Member: Scott Weiland>, <Member: Dave Kushner>, <Member: Matt Sorum>]
>>> Group.objects.all()
[<Group: Guns N' Roses>, <Group: Velvet Revolver>]

>>> axl = Member.objects.get(id=1)
>>> axl
<Member: Axl Rose>

>>> guns_and_roses = Group.objects.get(id=1)
>>> guns_and_roses
<Group: Guns N' Roses>

>>> axl_membership = Membership.objects.get(group=guns_and_roses, member=axl)
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
[<Member: Axl Rose>, <Member: Slash>, <Member: Duff McKagan>, <Member: Izzy Stradlin>, <Member: Steven Adler>]
>>> velvet_revolver.members.all()
[<Member: Slash>, <Member: Scott Weiland>, <Member: Dave Kushner>, <Member: Matt Sorum>, <Member: Duff McKagan>]

>>> Group.objects.filter(members__name__startswith='Slash')
[<Group: Guns N' Roses>, <Group: Velvet Revolver>]
```

## Django Rest Framework Practices

For make some practices the Django Rest Framework, please execute the following command:

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
>>> from webflix.models import TvSerie
>>> from webflix.serializers import TvSerieSerializer
>>> from rest_framework.renderers import JSONRenderer
>>> from rest_framework.parsers import JSONParser
>>> from datetime import datetime
>>> release_date = datetime.strptime('17-04-2011', '%d-%m-%Y').date()
>>> tv_serie = TvSerie(name='Game of Thrones', category='drama', release_date=release_date)
>>> tv_serie
<TvSerie: Game of Thrones>
>>> tv_serie.save()
>>> release_date = datetime.strptime('24-06-2015', '%d-%m-%Y').date()
>>> tv_serie = TvSerie(name='Mr. Robot', category='drama', release_date=release_date)
>>> tv_serie.save()
>>> serializer = TvSerieSerializer(tv_serie)
>>> serializer.data
{'category': u'drama', 'pk': 2, 'release_date': '2015-06-24', 'name': u'Mr. Robot', 'rating': 0}
>>> content = JSONRenderer().render(serializer.data)
>>> content
'{"pk":2,"name":"Mr. Robot","release_date":"2015-06-24","rating":0,"category":"drama"}'
>>> from django.utils.six import BytesIO
>>> stream = BytesIO(content)
>>> data = JSONParser().parse(stream)
>>> data
{u'category': u'drama', u'pk': 2, u'release_date': u'2015-06-24', u'name': u'Mr. Robot', u'rating': 0}
>>> serializer = TvSerieSerializer(data=data)
>>> serializer.is_valid()
True
>>> serializer.validated_data
OrderedDict([(u'name', u'Mr. Robot'), (u'release_date', datetime.date(2015, 6, 24)), (u'rating', 0), (u'category', u'drama')])
>>> tv_serie = serializer.save()
>>> tv_serie.save()
>>> TvSerie.objects.all()
[<TvSerie: Game of Thrones>, <TvSerie: Mr. Robot>, <TvSerie: Mr. Robot>]
>>> tv_serie.delete()
(1, {u'webflix.TvSerie': 1})
>>> TvSerie.objects.all()
[<TvSerie: Game of Thrones>, <TvSerie: Mr. Robot>]
>>> serializer = TvSerieSerializer(TvSerie.objects.all(), many=True)
>>> serializer.data
[OrderedDict([('pk', 1), ('name', u'Game of Thrones'), ('release_date', '2011-04-17'), ('rating', 0), ('category', u'drama')]), OrderedDict([('pk', 2), ('name', u'Mr. Robot'), ('release_date', '2015-06-24'), ('rating', 0), ('category', u'drama')])]
>>> 
```

# Reference

- [Django 1.9 Project tutorial](https://docs.djangoproject.com/en/1.9/intro/).
- [Django Rest Framework 3.6.4](http://www.django-rest-framework.org/#tutorial).
- [Introducción a Django Rest Framework](https://axiacore.com/blog/2012/06/introduccion-a-django-rest-framework/).
- [Levi Velázquez · Crear un API REST con Django Rest Framework - Parte I](http://levipy.com/crear-api-rest-con-django-rest-framework/).
- [Django 1.7 - introducción a Django REST Framework](http://blog.enriqueoriol.com/2015/01/django-1.7-intro-django-rest-framework.html).
- [Django REST Framework: Serializers anidados y ModelViewSet](http://blog.enriqueoriol.com/2015/03/django-rest-framework-serializers.html).
