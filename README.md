# Agenda

> A simple API for manager your contacts

## Table of contents
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Contact](#contact)

## Technologies
* Python - version 3.8
* Pipenv - version 11.9
* Django - version 3.1
* Django Rest Framework - version 3.12

## Setup
First Clone this repository and switch to the new directory

    $ git clone ...
    $ cd DjangoAPIAgenda

Active the Pipenv and instal requeriments

    $ pipenv install
    
Then apply migrations
    
    $ pipenv run python manage.py migrate
    
You can now run the development server

    $ pipenv run python manage.py runserver
        

## Features
List of features ready and TODOs for future development
* CRUD of contacts list

To-do list:
* Add Users and authentiations
* Add Image and owner to the contacts

## Status
_in progress_

## Contact
Created by [@diegojsanches](https://www.linkedin.com/in/diegojsanches/) - feel free to contact me!
