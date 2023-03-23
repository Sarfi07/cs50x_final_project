# Sangeetkar

Sangeetkar is a ```flask``` based web application which helps a group to share ideas and have conversation about it.
It is group platform to share thoughts and work on it.

### Descripton:

Sangeetkar uses PYTHON's ```flask``` framework. So, this description and usage of each file is mentioned below:

## helpers.py

This file is basically contains all the helpers function which is required in ```app.py``` file containing ```login_required``` and ```apology``` function. The former as imply that using this as decorator for the function will ensure that the user must be logged inn in order to use different concern function and the later function when something unauthorize happens gives back an error page with a customize message.



## app.py

file to be imported

    from flask import Flask, render_template, redirect, session, flash, request
    from flask_session import Session
    from werkzeug.security import check_password_hash, generate_password_hash
    from cs50 import SQL

    from helpers import login_required, apology
    from datetime import datetime


This ```app.py``` file contains all concern funtions for the application. functions such as **index, login, logout, register, create_card, chat and profile**. 

**Index function** works as a landing default page when the first enters into the site.

**login function** take input credentials from the user through a webpage and checks in the sqlite3 database and if the when return true then is let the user to log in.

**Log out function** logs the user out from the site

**Register** let the user to register themselves to site by filling up a form

**create_card function** is a feature impletmented to share content which every users on the site can see.

**chat feature** is implemented so that user can chat with themselves

**profile function** displays profile information about the user



## templates/
This folder contain all the html files that serves the application. This uses ```jinja``` templation language. Contianing files ```layout.html``` which works as base layout for all other html files.

## static/
static files such as images, logos, css files which doesnot change often as present in this folder.

# Design 

The design of the pages is kept simple .
it uses ```Bootstrap``` as css library for styling purposes which gives much of the responiveness.

Responsiveness: when opened on a laptop or desktop the navbar shows all the link and when viewed on a smaller screen the navbar shrinks and on the right top corner is a three dot button is presented, clicking on the button expands the navigation bar the exposes all the nav links.

The card feature on the homepage is a collapsible which uses some javascript as when clicked the content expands. It also has a ```Create card``` button which lets a user to create a card which can be seen by every other user.

**Profile** page displays all the information the user enters while registering process


## Database
This application uses sqlite3 as a database to information about pretty much every thing about the user. To prevent any **sql injection attacks** there is some code written in the backend to prevent it.