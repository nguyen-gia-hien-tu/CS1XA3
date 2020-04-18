# CS1XA3 Project03 - tun1

## Usage
* Install conda environment with `conda create -n djangoenv python=3.7`

* Run locally with `python manage.py localhost:8000` 
* Run on mac1xa3.ca server with `python manage.py localhost:100192`

* Log in with `TestUser`, password `1234`

## Objective 01
* __Description:__
    * This feature is displayed in <span style="color:blue">signup.djhtml</span> which is rendered by <span style="color:#ff4433">__signup_view__</span> function
    * It makes a POST request to `login:create_view` which is handled by <span style="color:#ff4433">__user_create_view__</span> function
    * The <span style="color:#ff4433">__user_create_view__</span> function will handle the POST request to create a new user, then automatically log the user in and redirect to `social:messages_view`

## Objective 02:
* __Description:__
    * This feature is displayed in <span style="color:blue">social_base.djhtml</span> which renders the __left_column__ used by <span style="color:blue">messages.djhtml</span>, <span style="color:blue">people.djhtml</span>, and <span style="color:blue">account.djhtml</span>
    * The template displays __real Profile and Interests__ (i.e. Username, Employment, Location, Birhtday, Interests) corresponding to the current logged in user 

## Objective 03:
* __Description:__
    * This feature is displayed in <span style="color:blue">account.djhtml</span> which is rendered by <span style="color:#ff4433">__account_view__</span> function
    * The <span style="color:blue">account.djhtml</span> includes a form for changing the password, and a form for updating user information (i.e. Employment, Location, Birthday, Interests)
    * For changing the password, it makes a POST request to `social:account_view` which is handled by <span style="color:#ff4433">__account_view__</span> function
        * After changing the password, the user will be logged out and redirected to `login:login_view` (i.e. they have to login again)
    * For updating the user information, the form makes a POST request to `social:update_view` which is handled by <span style="color:#ff4433">__update_view__</span> function
        * After updating the user information, the user will be redirected to `social:message_view` (the main page after the user logs in)

## Objective 04:
* __Description:__
    * This feature is displayed in <span style="color:blue">people.djhtml</span> which is redered by <span style="color:#ff4433">__people_view__</span> function
    * The page displays the list of people who are not friends with the current logged in user
    * The page starts out by displaying 1 people, then displays 1 more people by clicking the __More__ button
    * The __More__ button sends a POST request to <span style="color:#ff4433">__more_ppl_view__</span> function to add 1 more person to list of people will be displayed by keeping track of the number of people using a session variable name __`counter`__ and updating that session variable 
    * The number of people being displayed will be reset to 1 when the uer logs out by resetting the session variable in <span style="color:#ff4433">__logout_view__</span> in `login/views.py`

## Objective 05:
* __Description:__
    * This feature is displayed in <span style="color:blue">people.djhtml</span> which is rendered by <span style="color:#ff4433">__people_view__</span> function
    * The middle column is a list of "strangers" (people who are not friends with current logged in user)
    * All `FRIEND REQUEST` button are linked to a jQuery event with the class name of `.fr-button` to send a POST request to `social:friend_request_view` which is handled by the function <span style="color:#ff4433">__friend_request_view__</span>
    * The function <span style="color:#ff4433">__friend_request_view__</span> will handle the POST request and insert a new entry to the <span style="color:red">FriendRequest</span> model
    * After the current logged in user clicks the __FRIEND REQUEST__ button to send a friend request to a specific user, that __FRIEND REQUEST__ button will be disabled

## Objective 06:
* __Description:__
    * The right column of the page decribed in __Objective 05__ contains a list of people who sent the friend requests to the current user
    * The friend requests contain __Accept and Decline__ buttons
    * Pushing Accept or Decline button sends a POST request to `social:accept_decline_view` which is handled by <span style="color:#ff4433">__accept_decline_view__</span> function
    * The <span style="color:#ff4433">__accept_decline_view__</span> function handles the POST request and delete the corresponding __FriendRequest__ entry
    * If the friend request to the current logged in user is accepted, both of the user friends relations will be updated in the UserInfo table

## Objective 07:
* __Description:__
    * The feature is displayed in <span style="color:blue">messages.djhtml</span> which is rendered by <span style="color:#ff4433">__messages_view__</span> and <span style="color:#ff4433">__messages.js__</span>
    * The <span style="color:blue">messages.djhtml</span> displays all the the friends of the current user with their corresponding usernames

## Objective 08:
* __Description:__
    * The feature is displayed in <span style="color:blue">messages.djhtml</span> which is rendered by <span style="color:#ff4433">__messages_view__</span> and <span style="color:#ff4433">__messages.js__</span>
    * Pushing the `Post` button sends the content in the "Thoughts" (above the `Post` button) to `social:post_submit_view` which is handled by <span style="color:#ff4433">__post_submit_view__</span> function through AJAX POST request
    * The page will be reloaded upon a success response
    * The <span style="color:#ff4433">__post_submit_view__</span> function will handle the POST request and create a new __Post__ model object in the database

## Objective 09:
* __Description:__
    * The feature is displayed in <span style="color:blue">messages.djhtml</span> which is rendered by <span style="color:#ff4433">__messages_view__</span> function
    * The <span style="color:#ff4433">__messages_view__</span> function will query for posts and sort them from newest to oldest by __timestamp__
    * The page starts out by displaying 1 post and display 2 more posts each time the `More` button is clicked
    * Clicking the `More` button will send a POST request to <span style="color:#ff4433">__more_post_view__</span> function to add 2 more posts to list of posts will be displayed by keeping track of the number of posts using a session variable name __`post_counter`__ and updating that session variable 
    * The number of post being displayed will be rest to 1 when the user logs out by resetting the session variable in <span style="color:#ff4433">__logout_view__</span> in `login/views.py`

## Objective 10
* __Description:__
    * The feature is displayed in <span style="color:blue">messages.djhtml</span> which is rendered by <span style="color:#ff4433">__messages_view__</span> function
    * The feature allows the user to like the posts and display real life count
    * Pushing the `Like` button will send a POST request to `social:like_view` which is handled by <span style="color:#ff4433">__like_view__</span> function
    * The <span style="color:#ff4433">__like_view__</span> function adds the current user to the list of people who likes the post
    * The feature will also prevent the user from double-liking a post by disabling the __Like__ button
