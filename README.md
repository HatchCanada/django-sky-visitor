A full featured authentication and user system that extends the default Django contib.auth pacakge.

**Note:** Version 0.1.0. This library is under active development. While in active development, the API will be changing frequently.


# Features

  * Subclass the User model to add your own fields, making queries easier to write
  * Class-based view implementations of all of the views
  * Email-based authentication. Entirely hides username from the user experience and allows an email-focused experience.
  * Invitations
  * Password rules


# Usage
Throughout this app, any class beginning with `Email` indicates that it is for use with email-only authentication systems.
In all cases, there should be a matching class without `Email` at the beginning of the class name that is for use with username-focused authentication systems.


## Quickstart

  * `pip install PACKAGEPATHHERE`
  * Add `custom_user` near the top of your `INSTALLED_APPS` setting
  * Somewhere in your own `myapp.models.py`, define one of the two following code blocks:

```python
# Assume this is in myapp.models
from custom_user import EmailCustomUser, EmailUserManager

class User(EmailCustomUser):
    objects = EmailUserManager()
```

  * In your're `settings.py` add these lines:

```python
# Change myapp to the name of the app where you extend EmailCustomUser
CUSTOM_USER_MODEL = 'myapp.User'
AUTHENTICATION_BACKENDS = [
    'custom_user.backends.EmailBackend',
]

# Add this line to your INSTALLED_APPS
INSTALLED_APPS = [
    'custom_user',
    # ...
]

# Specify a URL to redirect to after login
LOGIN_REDIRECT_URL = '/'
```


## Advanced usage

  * Override URLs and views to provide custom workflows
  * Custommize views and URLs
  * Customize forms
  * Choose to not automatically log a user in after they compelte a registration, or password reset
  * Don't create users with `manage.py createsuperuser` or `django.contrib.auth.models.User.create_user()` because there won't be a proper entry in the subclassed user table for them
  * On EmailCustomUser you can set `validate_email_uniqeness` to false if you're concerned about the extra database query for each call to clean()

### Messages
This app uses the [messages framework](https://docs.djangoproject.com/en/dev/ref/contrib/messages/) to pass success messages
around after certain events (password reset completion, for example). If you would like to improve the experience for
your users in this way, make sure you follow the message framework docs to enable and render these messages on your site.


# Settings
Must specify `SECRET_KEY` in your settings for any emails with tokens to be secure (example: invitation, confirm email address, forgot password, etc)


# Admin
By default, we remove the admin screens for Auth User and place in an auth screen for you authentication

If you want to re-add the the django contrib user, you can do that by re-registering django.contrib.auth.User

If you want fine-grained control over the admin you can subclass the custom_user `UserAdmin`:

```python
from custom_user.admin import UserAdmin

class MyUserAdmin(UserAdmin):
   # Your code here
   pass

admin.site.register(MyUser, MyUserAdmin)
```


# Background
One of the problems this module was created to solve is the challenge presented when you want to store additional information
about the user. The Django docs [suggest](https://docs.djangoproject.com/en/dev/topics/auth/#storing-additional-information-about-users)
having a `UserProfile` model with a OneToOneField to `User`. This makes queries more straight forward. In the background,
Django automatically does an inner join between contrib.auth.Models and your subclassed user model via
[proxy models](https://docs.djangoproject.com/en/dev/topics/db/models/#proxy-models).


# Roadmap

Development TODO list:

  * Invitation clean up and tests

Features to add:

  * Admin login form should handle email-only authentication
  * Email confirmation on registration
  * Implement `LOGOUT_REDIRECT_URL`
  * Better built in password rules. Options for extending the password rules.
  * Refactor token URL generation to `utils.py`
  * Change email form and email confirmation page

Improvements to documentation:

  * Change PACKAGEPATHHERE in the quickstart guide
  * Step by step of password reset process and how it works


# Author
Built at [Concentric Sky](http://www.concentricsky.com/) by [Jeremy Blanchard](http://github.com/auzigog/).


# License
Copyright 2012 Concentric Sky, Inc. This project is licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).


