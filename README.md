# MasterGame


## Table of Contents

1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Folder Structure](#folder-structure)
4. [Views](#views)
    - [IndexView](#indexview)
    - [DashboardView](#dashboardview)
    - [RegisterView](#registerview)
    - [UserSettingsView](#usersettingsview)
    - [AddSessionView](#addsessionview)
5. [Models](#models)
    - [GameMaster](#gamemaster)
    - [Player](#player)
    - [GameSession](#gamesession)
    - [GameSystem](#gamesystem)
    - [PlayerCharacter](#playercharacter)
    - [CharacterSheet](#charactersheet)
6. [Forms](#forms)
    - [LoginForm](#loginform)
    - [UserRegistrationForm](#userregistrationform)


## Project Overview

Master Game is an application that allows to create, organize and manage RPG sessions.
Current version allows to register a new user, log in, change permissions and add new game sessions.

## Technologies Used

This section provides an overview of the technologies and tools used in the development of this Django project:

- **Framework**: Django 4.2.4
- **Front-End**: HTML/CSS, JavaScript, Bootstrap
- **Database**: PostgreSQL
- **Version Control**: Git
- **Development Environment**: Python, Virtual Environment
- **Testing**: pytest 7.4.0 and pytest-django 4.5.2
- **Deployment**: TO BE DONE
- **Additional Libraries**: Various Python libraries and Django packages

## Folder Structure

Folder structure of the project:
```
MasterGame
├── GameMaster_app/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── MasterGame/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tests/
│   ├── conftest.py
│   ├── pytest.ini
│   └── test_django.py
├── manage.py
└── README.md
```

## Views

### IndexView

The `IndexView` handles the rendering of the index page and user login functionality.

### DashboardView

The `DashboardView` is responsible for displaying the user's dashboard.

### RegisterView

The `RegisterView` handles user registration and account creation.

### UserSettingsView

The `UserSettingsView` allows users to modify their account settings.

### AddSessionView

The `AddSessionView` allows users to create new game sessions.


## Models

### GameMaster

The `GameMaster` model represents game masters and their related data.

### Player

The `Player` model represents players and their related data.

### GameSession

The `GameSession` model stores information about game sessions.

### GameSystem

The `GameSystem` model stores information about game systems used in sessions.

### PlayerCharacter

The `PlayerCharacter` model represents player characters in the game.

### CharacterSheet

The `CharacterSheet` model stores character attributes and statistics.


## Forms

### LoginForm

The `LoginForm` handles user login and includes fields for username and password.

### UserRegistrationForm

The `UserRegistrationForm` allows users to register and create accounts with username, first name, and email.
