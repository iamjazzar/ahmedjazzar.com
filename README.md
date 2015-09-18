# ahmedjazzar.com
My personal website source code. More info will be [here](http://www.ahmedjazzar.com).

# Website status
UNDERDEVELOPMENT

# Development
ahmedjazzar.com is a simple personal website powered by Django framework.
ahmedjazzar.com is written using the hackable text editor - [Atom](https://atom.io/).

## Repo. files overview
* [ahmedjazzar](https://github.com/ahmedaljazzar/ahmedjazzar.com/tree/master/ahmedjazzar): Django server settings.
* [templates](https://github.com/ahmedaljazzar/ahmedjazzar.com/tree/master/templates): the templates used to generate dynamic html pages.
* [static](https://github.com/ahmedaljazzar/ahmedjazzar.com/tree/master/static): additional files such as images, styles, or fonts.
* [ahmedjazzarcom](https://github.com/ahmedaljazzar/ahmedjazzar.com/tree/master/ahmedjazzarcom): app dir.

## Getting the Code

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ git clone git@github.com:ahmedaljazzar/ahmedjazzar.com.git`

## Installation
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ sudo add-apt-repository ppa:chris-lea/node.js`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ sudo apt-get update`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ sudo apt-get install nodejs python-virtualenv libmysqlclient-dev python-dev`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ mkvirtualenv ajazzar -r requirements.txt`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ npm install`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ bower install`

## Database
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ CREATE DATABASE ahmedjazzar;`

## Run the development server
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ workon ajazzar`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ cd to/the/project/root`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ python manage.py runserver --settings=ahmedjazzar.dev`

## Run gulp
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ gulp`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`$ gulp watch`

# Homepage
![homepage](https://s3.amazonaws.com/upload.screenshot.co/70055694b4)

# License
The MIT License (MIT)
Copyright (c) 2015 Ahmed Jazzar <ahmed.mojaz@gmail.com>
