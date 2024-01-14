# Hive Management

## Getting started
This is a project realised for my formation at Diginamic, in order to obtain the title of Appliation Conceptor and Developper, specializefd in Python and Angular.Here I have practice my knowledge about Django and DjangoRestFramework.

This is the back-end of a Hive Management application.

You can here login, create your beeyard(s), hive(s), and the interventions on them.  


## Dependencies
For this project, the following file has to list the python dependencies of your project.
- **requirements.txt** set your app dependencies here and set version requirements if needed.


## About environment
The file named **.env-template** list the required environnement variables that your project need, but **does not** contains any citical informations such as credentials. It can contains **example values**. It's purpose is to show how to build the **.env** file.

The **.env** needs to be listed in the **.gitignore**, it's **not versionned**, it's **only in your system**.


***
## Configuration
List here the steps to follow to run the application.
- You need to have access to a PostgresQL database
- Install the dependencies from requirements.txt (maybe in a virtual environment)
- Create you .env file based on .env-template

## How to use
Run the following command to launch the Django server :
- `python manage.py migrate`
- `python manage.py createsuperuser`
- `python manage.py runserver`

The pages are :
- `url/admin` (if you use a superuser)
- `url/beeyard` will show the list of your beeyards, clickable.
- `url/beeyard/id` will show the list of hive in a specific beeyard.
- `url/intervention` will show the list of interventions you've created with your logged-in account.


***
## Troubleshooting
You can list here, if needed, the common issues that the users of your app can encounter.