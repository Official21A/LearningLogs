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

$ >> python OR python3 -m venv lib:name

This will help you manage libraries needed for project and will let you easily find theme with
a single commandl line:

$ >> pip OR pip3 freeze > output.txt

The following command will get all of the external libraries you used for the project and will save
them into "/output.txt".
After you create your library you have to activate it via:

$ >> source lib:name/bin/activate

And we your done just enter:

$ >> deactivate

# Creation
To let the django start we use following command-line:

$ >> django-admin startproject project:name .

# Data base
Each web-app uses a data base of its own the is not human readable
and only means something for the compiler.
Data base is the most important file of your app, cause it saves all of the information you enter for
your web-app. Loosing your data base file will reset all of the settings (Superadmin- Users- Groups- Users data- ...)
back to default.

For creating a data base file enter following command-line:

$ >> python OR python3 manage.py migrate

# Running local server
Django uses your own system as a server for itself. You can manully put your web-app into an online server (like Heroka)
to let anyone access to your web-app via URL.
To run a local server enter following command-line:

$ >> python OR python3 manage.py runserver

p.s. To see if your server is running, open a browser tab and enter https://localhost:8000/ or https://127.0.0.1:8000/

# Defining models
All of the Objects that we want to use in our web-app should be defined in "/models.py".
