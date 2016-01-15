# ahmedjazzar.com
My personal website source code. [More info](http://www.ahmedjazzar.com).

# Website status
RELEASED

# Development
ahmedjazzar.com is a simple personal website powered by Django framework, developed on Docker.
ahmedjazzar.com is written using the hackable text editor - [Atom](https://atom.io/).

## Repo. files overview
* [ahmedjazzar](https://github.com/ahmedaljazzar/ahmedjazzar.com/tree/master/ahmedjazzar): Django server settings.
* [templates](https://github.com/ahmedaljazzar/ahmedjazzar.com/tree/master/templates): the templates used to generate dynamic html pages.
* [static](https://github.com/ahmedaljazzar/ahmedjazzar.com/tree/master/static): additional files such as images, styles, or fonts.
* [ahmedjazzarcom](https://github.com/ahmedaljazzar/ahmedjazzar.com/tree/master/ahmedjazzarcom): app dir.

## Getting the Code

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ git clone git@github.com:ahmedaljazzar/ahmedjazzar.com.git`


## Run the development server
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ cd ahmedjazzar.com`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ docker-compose up`

Inside docker web continer run:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ python manage.py migrate --settings=ahmedjazzar.dev`


## Run gulp
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ gulp`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ gulp watch`

# License
GNU AFFERO GENERAL PUBLIC LICENSE
Copyright (c) 2016 Ahmed Jazzar <me@ahmedjazzar.com>
