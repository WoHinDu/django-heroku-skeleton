# Django Heroku Skeleton
## About

A Django skeleton for Django 1.10.3. Build for work with Heroku. In just 15 
minutes you get a running Django instance on Heroku.

## 0. Pre
### Notation

In this readme replace:
- myproject with your project name
- myapp with your app name
- yoursecretkey with your secret key
- myapplink with your Heroku link
- herokuappname with the name from your Heroku instance
- githubname with your GitHub username
- githubrepo with the name from your (new) repo
- privatesentrydsn with your **_private_** Sentry dsn from [sentry.io](https://sentry.io/)
- publicsentrydsn with your **_public_** Sentry dsn from [sentry.io](https://sentry.io/)

### For Linux:
- TBD

### For Windows:
- Install Windows PowerShell [Link](https://github.com/PowerShell/PowerShell/blob/master/docs/installation/windows.md#msi)
- Install Python 3 [Link](https://www.python.org/downloads/windows/)
- Install pylauncher [Link](https://bitbucket.org/vinay.sajip/pylauncher/downloads)
- Install Heroku Toolbelt [Link](https://devcenter.heroku.com/articles/heroku-command-line#download-and-install)
- Install and configure git [Link](https://help.github.com/articles/set-up-git/)

Open PowerShell as Administrator and execute ```Set-ExecutionPolicy Unrestricted``` 
answer with yes. Close Powershell. (Necessary for virtualenv)

Open PowerShell with normal limited rights.

Login into Heroku
```
heroku
```

Install virtualenv
```
pip install virtualenv
```

Install actual Django version
```
pip install django
```

## 1. Let's start

Navigate in the console to the folder where you want to have your Django project. Then create your project and your app.
```
django-admin startproject --template=https://github.com/WoHinDu/django-heroku-skeleton/archive/master.zip  --name Procfile,requirements.txt myproject
cd myproject
python manage.py startapp myapp
```

- Open `myproject\settings\base.py` in your editor and add `'myapp.apps.MyappConfig',` in the 
first line from `INSTALLED_APPS`.
- Open `myproject\settings\prod.py` in your editor and replace `myapp` in LOGGING
- Open `myproject\settings\dev.py` in your editor and replace `myapp` in LOGGING

Remove unnecessary stuff
``` 
rm readme.md
```

Create folder for static assets and templates
```
mkdir myapp\templates
mkdir myapp\static
```

Create a virtualenv called "venv"
```
virtualenv venv
```

Activate virtualenv

For Windows
```
.\venv\Scripts\activate
```

For Linux
```
source venv/bin/activate
```

To deactivate it later just type:
```
deactivate
```

Install required stuff
```
pip install -r myproject/reqs/dev.txt
```

## 2. Run your site
Migrate database
```
python manage.py migrate
```

Spin up the development server
```
python manage.py runserver
```

Open it in your web browser and enjoy it :)

## 3. Deploy to Heroku

Create empty git repo
```
git init
```

Create Heroku app
```
heroku create myproject --region eu
```

Create new GitHub repo at [github.com](https://github.com). Then connect it 
with your new local git repo.
```
git remote add github git@github.com:githubname/githubrepo.git
```

Open with `git config -e` the configuration file from your local git repo and
add at the end the following:
```
[remote "origin"]
	pushurl = git@github.com:githubname/githubrepo.git
	pushurl = https://git.heroku.com/herokuappname.git
```
You are now able to push with just one command your stuff to GitHub and Heroku.

Open `myproject\settings\prod.py` and copy your Heroku-app link in  `ALLOWED_HOSTS = ['.myapplink']`. 
The leading dot is important! (Without https://)

Set environment variables in Heroku
```
heroku config:add SECRET_KEY=yoursecretkey
heroku config:add DJANGO_SETTINGS_MODULE=myproject.settings.prod
```

Create an account at [sentry.io](https://sentry.io/). Create an organisation
and project. Then add your Sentry DNS code as an environment variable.
```
heroku config:add SENTRY_DSN=privatesentrydsn
```

Open `temlates/500.html` and replace `publicsentrydsn` with your **_public_** DSN from Sentry.

Note: Sentry is also available as a Heroku Addon, but unfortunately no longer as a free version.

Add Heroku modules. I choose for every module the free plan, but this can
change from time to time. Please check it twice at [Heroku](https://elements.heroku.com/addons).

Deploy Postgres. An amazing database. For more info see [Postgres](https://elements.heroku.com/addons/heroku-postgresql	)
```
heroku addons:create heroku-postgresql:hobby-dev
```

Deploy Papertrail. Allows you to view the logs from your app/Heroku. For more info see [Papertrail](https://elements.heroku.com/addons/papertrail)
```
heroku addons:create papertrail:choklad	
```

Deploy Sendgrid. It allows you to send emails. For more info see [Sendgrid](https://elements.heroku.com/addons/sendgrid)
```
heroku addons:create sendgrid:starter
```

Deploy Librato. It monitors everything on Heroku for you. For more info see [Librato](https://elements.heroku.com/addons/librato)
```
heroku addons:create librato:development
```

Add anything to git, commit and push it.
```
git add -A
git commit -m "Initial commit"
git push origin master
```

Now go to `https://dashboard.heroku.com/apps/herokuappname/deploy/github`
and connect your GitHub repo with Heroku.

Migrate database
```
heroku run python manage.py migrate
```

Create a superuser for your project
```
heroku run python manage.py createsuperuser
```

Finished! Enjoy your new Heroku site. If you have any remarks, improvements or
anything else, I'm happy about every pull request/opened issue!

```
heroku open
```

# What else?
Now you have a running Django instance on Heroku. That means you can start
developing your project. If you are satisfied with django-heroku-template, 
you can now stop configuring and start coding. If not, here a few
ideas, who are maybe helpful for you:
- edit the settings files to your preferred settings
- [Localise](https://docs.djangoproject.com/en/1.10/topics/i18n/) your project
- Setup your own [domain](https://devcenter.heroku.com/articles/custom-domains)
- Add your own [SSL certificate](https://devcenter.heroku.com/articles/ssl)
- Set up a continuous integration system like [Travis](https://travis-ci.org/)
- Link [Sentry](https://docs.sentry.io/integrations/github/) with your [GitHub](https://github.com/) repo
and activate release tracking
- Use a Content-Delivery Network with [WhiteNoise](http://whitenoise.evans.io/en/stable/django.html#use-a-content-delivery-network)
- Include [caching](https://devcenter.heroku.com/articles/django-memcache) and 
[compressing](https://github.com/django-compressor/django-compressor)
- Use an asynchronous task queue like [Celery](http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html)
in connection with [CloudAMQP](https://elements.heroku.com/addons/cloudamqp)
- Serve your static assets via [Amazon S3](https://github.com/kennethreitz/dj-static)
- ...

# Credits
I borrowed a few ideas from guys who are a way more familiar with Python and
Django than I am. Thanks to:
- [rdegges](https://github.com/rdegges) especially for his [django-skel](https://github.com/rdegges/django-skel)
- [heroku](https://github.com/heroku) for the amazing infrastructure and the [heroku-django-template](https://github.com/heroku/heroku-django-template)
- [etianen](https://github.com/etianen) especially for his [django-herokuapp](https://github.com/etianen/django-herokuapp)
