# Hive Management - Lil Fumanal

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


The API :
- `url/admin` (if you use a superuser)
- `url/beeyard` will show the list of your beeyards, clickable.
  GET: will display all your beeyards.
  POST: will add a beeyard. Required params: {name: value}
- `url/beeyard/id` will show the list of hive in a specific beeyard.
  GET: will show the list of hives.
  POST: will add a hive in the specified beeyard.
    Required params: {
      name: str_value,
      status: choice_value,
      queen_age: int_value,
      bee_type: choice_value,
    }
- `url/intervention` will show the list of interventions you've created with your logged-in account.
  GET: will display all your interventions.
  POST: will add an intervention.
    Required params: {
      hive: hive_id,
      motif: choice_value,
      harvest_quantity: int_value (optionnal),
      is_sick: bool_value,
      decease: str_value(optionnal)
      }


***
## Troubleshooting
- `url/beeyard/id/interventions` were supposed to be a post url to add the same interventions to all hives from a specific beeyard.
- It may appears that a lot of post request don't have the permission to be posted, even with permission.AllowAny or IsAuthenticated. 
- I didn't success to create the script behind the command `python manage.py import`, but it's still accessible so you can put another one's functionnal script and still not waste much time. I also left the tables .csv in the Database_datas directory.
