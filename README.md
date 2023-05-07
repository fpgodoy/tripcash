# Tripcash <h1>

## Overview
  Tripcash is a Python-based web application designed to manage your trip finances. It enables you to easily register all your expenses and then view them by date and label, either in a list or summed up.

  This application is the result of my final project for the [CS50 course](https://cs50.harvard.edu/x/2021/), and it was created to address my own struggles with managing trip expenses. The development was guided by the [official Flask documentation](https://flask.palletsprojects.com/en/2.0.x/tutorial/) and optimized for deployment on Heroku.com.

  To make it simple and fast to use, the application doesn't have any images or JavaScript. All the CSS is made using Bootstrap. To deploy it using Heroku, it was needed to use PostgreSQL instead of SQLite3.
  
  Unfortunately, the application demo is no longer available as Heroku has shut down the free instances.

## Features
  Here are some of the key features of Tripcash:
  * User authentication: Tripcash allows you to register and log in to your account, so you can keep track of your expenses and trips.
  * Trip management: With Tripcash, you can create, edit, and delete trips, and keep all your expenses organized by trip.
  * Label management: Tripcash comes with four default labels (Food, Transport, Tickets, and Accommodation), but you can create, edit, and delete your own labels to better fit your travel needs.
  * Expense tracking: Tripcash lets you register all your travel expenses, including the date, label, description, and amount, and view them in a list or by label and date. You can also edit or delete your expenses if you need to make any changes.
  
## Files
  * **'auth.py'**: Contains all the authentication functions, including Login, Logout, Register User, and Change Password.
  * **'db.py'**: Includes the DB connection and all the DB query to create the tables and their functions.
  * **'expense.py'**: Contains the function to create a new expense.
  * **'home.py'**: Contains functions to the index and welcome page.
  * **'label.py'**: Contains all the functions to create, edit, list, and delete the labels.
  * **'list.py'**: Contains the function to list existing expenses, delete or edit them, and the function to sum and list the expenses by label and date.
  * **'Procfile'**: Declares the process types and command to run the app on the Heroku.com platform.
  * **'requirements.txt'**: Lists all the dependencies needed to run the app.
  * **'/templates/'**: Contains all the HTML pages to render using the base.html file.
