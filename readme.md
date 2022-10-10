# django-stock-app (capstone) 
<!-- Please update value in the {}  -->

<h1 align="center">Django Stock App</h1>

<div align="center">
  <h3> 
    <a href="https://github.com/esadakman/django-stock-app">
      Project
    </a> 
  </h3>
</div>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Acknowledgements](#acknowledgements)
- [Informations](#informations)
- [Entity Relationship Diagram](#entity-relationship-diagram)
- [Overview](#overview)
- [Built With](#built-with)
- [Project Structure](#project-structure)
- [How to use](#how-to-use)
- [Contact](#contact)


## Acknowledgements

- I created a Stock Manegement API with Django Rest Framework that allows users to
    - register/login/logout
    - CRUD operations for Product,Transaction,Firm, Brand, and Category acoording to user's role

## Informations

##### User Roles (You can set it from the admin panel.)

  - Manager:
    - Authorized all CRUD operations in Stock App 
  - Product_Manager:
    - Authorized all CRUD operations in Category, Brand, Firm, Product tables
  - Finance:
    - Authorized all CRUD operations in Transaction table and read only other tables
  - Read_Only:
    - Authorized only read operations in all tables

##### Transactions Operations

  - Transaction field, which in Transaction table, determines the type of stock object. 
  - If the transaction is 'IN' stock of product object is recalculating.
  - If the transaction is 'OUT' we are checking stock of product in Product table if there is enough stock. In the case of does not enough stock in product we are raising ValidationError otherwise we are recalculating the stock of product object.
  - Price_total field, which in Stock table, is read_only field and we are calculating this value with quantity and price fields.
  - All views have filter and search features. 
  - In addition to the filters in category views we have also nested serializer which shows us products belonging to categories. 

<!-- ERD -->
## Entity Relationship Diagram

![Entity Relationship Diagram](https://user-images.githubusercontent.com/98649983/194851017-083393e4-53ef-425d-869c-903d8515fdaa.jpg)
 
 <!-- OVERVIEW -->
## Overview

![stock-app](https://user-images.githubusercontent.com/98649983/194851648-3e22780b-7e5c-481f-aabc-facc261b485b.gif)




### Built With

<!-- This section should list any major frameworks that you built your project using. Here are a few examples.-->

- Django
- Django Rest Framework
- Django Rest Auth
- Django Nested Admin
- Django Debug Toolbar
- Django Filter 
- PosrtgreSQL
- Swagger

## Project Structure

```bash
.──── django-stock-app (repo)
│
├── main
│     ├── __pycache__ 
│     ├── __init__.py 
│     ├── asgi.py
│     ├── urls.py
│     ├── wsgi.py
│     └── settings
│           ├── __pycache__
│           ├── db.sqlite3
│           ├── __init__.py 
│           ├── base.py
│           ├── dev.py 
│           └── prod.py
│─── stock
│       ├── __pycache__
│       │── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py 
│       ├── signals.py
│       ├── permissions.py 
│       ├── serializers.py 
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├──── users
│       ├── __pycache__
│       ├── migrations
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── serializers.py
│       ├── signals.py 
│       ├── tests.py
│       ├── urls.py
│       └── views.py 
├── manage.py
├── db.sqlite3
├── debug.log
├── requirements.txt
└── .env

```

## How To Use 

To clone and run this application, you'll need [Git](https://git-scm.com)

```bash
# Clone this repository
$ git clone https://github.com/esadakman/django-stock-app 

# Install dependencies
    $ python -m venv env
    > env/Scripts/activate (for win OS)
    $ source env/bin/activate (for macOs/linux OS)
    $ pip install -r requirements.txt 

# Add .env file for secret key, ENV_NAME and SQL informations 

- Create a .env file for =>
  -- SECRET_KEY,
  -- ENV_NAME  
  -- DEBUG value, 
  -- SQL_DATABASE,
  -- SQL_USER,
  -- SQL_PASSWORD,
  -- SQL_HOST and
  -- SQL_PORT values

- After these you can run the project as usual => 

# Run the app
    $ python manage.py runserver
```

## Contact

- Website [@esadakman](https://esadakman.github.io/)
- GitHub [@esadakman](https://github.com/esadakman)
- Linkedin [@esadakman](https://www.linkedin.com/in/esadakman/)

 