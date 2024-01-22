# Python - School Admin application

## Codecademy portfolio project - Python

### Introduction
This is a simple application written as a Portfolio Project for the Intro to Python course on Codecademy

The application allows Admins, Teachers, and Students to keep track of Subjects in a school context

### Classes
#### Admin
This is a class of user is able to:
* CRUD Teachers, Students and Subjects
* Assign Teachers to Subjects
* Enrol Students in Subjects

#### Teacher
This is a class of user who is able to:
* Deliver lessons

#### Student
This is a class of user who is able to:
* Attend lessons

#### Subject
This class represents the various subjects or courses offered by the School

### Application
The basic application requires a user to 'login' by identifying his/her role and user account - which is validated against an existing list. The application uses a static permissions dictionary to present a roele-based menu to each user role - which is navigated by providing the index of the required menu item. Each menu item gathers validated input from the user to identify the objects required as parameters for each method.

### Functions
As far as possible, features has been represented in functions to maximise the reusability of the code and make maintenance easier. I tried to find a balance between abstraction and readability - and not sure I succeeded!
