# LearningLogs
Creating a web-app using python usefull framework "Django".

# Intro
Using "Django" framework requiers some external libraries which are recommended in
"/requirements.txt".

After donwloading and installing django on your python you need some command orders
to create data base and the admin/user for your web-app and then modify your Manual Objects
for the app.

# Starting
It is better to create a source lib for your project and add the external libraries you need
for your project init:

```
python OR python3 -m venv lib:name
```

This will help you manage libraries needed for project and will let you easily find theme with
a single commandl line:

``` 
pip OR pip3 freeze > output.txt 
```

The following command will get all of the external libraries you used for the project and will save
them into "/output.txt".
After you create your library you have to activate it via:

``` 
source lib:name/bin/activate 
```

And we your done just enter:

``` 
deactivate 
```

# Creation
To let the django start we use following command-line:

```
django-admin startproject project:name . 
```

# Data base
Each web-app uses a data base of its own the is not human readable
and only means something for the compiler.
Data base is the most important file of your app, cause it saves all of the information you enter for
your web-app. Loosing your data base file will reset all of the settings (Superadmin- Users- Groups- Users data- ...)
back to default.

For creating a data base file enter following command-line:

``` 
python OR python3 manage.py migrate 
```

# Running local server
Django uses your own system as a server for itself. You can manully put your web-app into an online server (like Heroka)
to let anyone access to your web-app via URL.
To run a local server enter following command-line:

``` 
python OR python3 manage.py runserver 
```

p.s. To see if your server is running, open a browser tab and enter https://localhost:8000/ or https://127.0.0.1:8000/

# Defining models
All of the Objects that we want to use in our web-app should be defined in "/models.py".
We write our classes in this file then we need to active and migrate them, so we can use them in our app.
After creating them we go to "/settings.py" and in the INSTALLED_APPS list we add our project name.
Then we save it and we migrate the project by these following commands:

```
python OR python3 manage.py makemigrations project:name 
python OR python3 manage.py migrate 
```

Now that we migrate our models we need to register them with the admin site.
First we create an admin for our site with following command:

``` 
python OR python3 manage.py createsuperuser 
```

The following command will create a "/admin.py" file for us. Open it and add import your models, then write:

admin.site.register(Class:name)

Now if you enter https://localhost:8000/admin/ you can see your registerd classes with admin.
So each time we add a new class for the web-app we do the following steps:

1.Modify the models.py

2.manage.py makemigration project:name

3.manage.py migrate

4.Register in "/admin.py"

# Shell
Django has a shell mode for the web-apps where you can test the app without actually opening browser or ....
Just enter:

```
python OR python3 manage.py shell 
```

And for quiting enter ctrl+D.

# Users
Like the admin, the users need some source files.
We create them by entering the following command:

``` 
python OR python3 manage.py startapp users 
```

This will create the users folders for us to manage the web-app users.
Again we need to go to the "/settings.py" and add the following folder to the INSTALLED_APPS list.

# Finally
So the base part of the project is done here, rest is just connected to the usage of your web-app.
These steps will lead you to create the basics for a web-app and the rest is just depends on you.

# Project-Explain
In this project we have a site that users can come and Register or maybe Logging in. Then they can access their own
special data, manage them and log out.
For the web pages I used Bootstrap4 and the sql data base. Easy to use and easy to setup.

Thank you.

### Contact me at : najafizadeh21@gmail.com
