# CRUD APP GITHUB OAUTH


A simple application where you can login with Oauth as Gitlab as your provider and update your profile information.

  - Login with your Github account
  - Update your profile information
  - Magic!

# Features!

  - Create your profile using Gitlab 
  - Update your profile personal information
  - Delete your profile


### Tech

This app uses a number of open source projects to work properly:

* [Python] - Version 3.7.3
* [Django] - Version 3.0.4


### Installation

Installation is fairly simple
 - git clone the repo



This app is running on Python 3.7.3 so lets create a virtualenv that matches that version and install dependencies


Create a virtualenv install requirements
```sh
$ virtualenv env
$ cd env/Script
$ activate
(env)$ pip intall -r requirements
```

Next we need to create a local_settings.py in the same directory where settings.py is
Because this application requires Github Oauth to login it requires the following global variables to be inside local_settings.py
```sh
SOCIAL_AUTH_GITHUB_KEY = '123zxy123zxy123zxy'
SOCIAL_AUTH_GITHUB_SECRET = '123zxy123zxy123zxy'
```
You can make an app and get a Key and a Secret in [GitHub Applications]


### Development

Add more ways to sign in for example using; Google, Twitter and Facebook.

### Docker

In development 




### README

Readme was created using [Dillinger] 


**Free Software, Hell Yeah!**

   [dill]: <https://github.com/joemccann/dillinger>
   [Dillinger]: <https://dillinger.io/>
   [Python]: <https://www.python.org/downloads/release/python-373/>
   [Django]: <https://docs.djangoproject.com/en/3.0/releases/3.0.4/>
   [GitHub Applications]: <https://github.com/settings/applications/new>
 
