# Udacity_FSND_Project4  - **CATALOG DB -- Charitable Goods Inventory** by Jason M. Hester
==============================

## Required Libraries and Dependencies
-----------------------------------
This program runs on Python 2.7 and requires a working Vagrant Linux Virtual Server with SQLite and Flask.

## How to Run Project
------------------
1. Download the fullstack-nanodegree-vm repository, unzip, and install in a folder of your choosing under the /vagrant directory.
2. Open a Terminal and run the following commands:
        vagrant ssh
        cd vagrant/<your chosen folder>
        python database_setup.py
        python databse-init.py
        python application.py
3. Open a browser instance and navigate to localhost:8000

## Description
-----------
This program uses python to run a database server with CRUD finctionality and JSON endpoints in order to do the following:
        1. Login with google plus or facebook
        2. View a list of locations and their charitable goods inventory
        3. Create and Edit locations and charitable items
        4. Update and Delete locations and charitable items
        5. Display the information in an html page