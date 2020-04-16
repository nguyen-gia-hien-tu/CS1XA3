# CS1XA3 Project03 - tun1

## Usage
* Install conda environment with `conda create -n djangoenv python=3.7`

* Run locally with `python manage.py localhost:8000` 
* Run on mac1xa3.ca server with `python manage.py localhost:100192`

* Log in with TestUser, password 1234

## Objective 01
* __Description__:
    * This feature is displayed in `signup.djhtml` which is rendered by `signup_view` function
    * It makes a POST request to `login:create_view` which is handled by `user_create_view` function
    * The `user_create_view` function will handle the POST request to create a new user, then automatically log the user in and redirect to `social:messages_view` page

## Objective 02:
* __Description__:
    * This feature is displayed in `social_base.djhtml` which renders the __left_column__ used by __messages.djhtml__, __people.djhtml__, and __account.djhtml__
    * The template displays __real Profile and Interests__ (i.e. Username, Employment, Location, Birhtday, Interests) corresponding to the current logged in user 

## Objective 03:
* __Description__:
    * This feature is displayed in `account.djhtml` which is rendered by `account_view` function
    * The `account.djhtml` includes a form for changing the password, and a form for updating user information (i.e. Employment, Location, Birthday, Interests)
    * For changing the password, it makes a POST request to `social:account_view` which is handled by `account_view` function
        * After changing the password, the user will be logged out and redirected to `login:login_view` (i.e. they have to login again)
    * For updating the user information, the form makes a POST request to `social:update_view` which is handled by `update_view` function
        * After updating the user information, the user will be redirected to `social:message_view` (the main page after the user logs in)

## Objective 04:
* __Description__:
    * This feature is displayed in `people.djhtml` which is redered by `people_view` function
    * The page displays the list of people who are not friends with the current logged in user
    * The page starts out by displaying 1 people, then displays 1 more people by clicking the __More__ button
    * The __More__ button sends a POST request to `more_ppl_view` function to add 1 more person to list of people will be displayed

## Objective 05:
* __Description__:
