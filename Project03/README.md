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
    * This feature is displayed in `social_base.djhtml` wich renders the __left_column__ used by __messages.djhtml__, __people.djhtml__, and __account.djhtml__
    * The template displays __real Profile and Interests__ (i.e. Username, Employment, Location, Birhtday, Interests) corresponding to the current logged in user 