from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages

from . import models, forms

def messages_view(request):
    """Private Page Only an Authorized User Can View, renders messages page
       Displays all posts and friends, also allows user to make new posts and like posts
    Parameters
    ---------
      request: (HttpRequest) - should contain an authorized user
    Returns
    --------
      out: (HttpResponse) - if user is authenticated, will render private.djhtml
    """
    if request.user.is_authenticated:
        user_info = models.UserInfo.objects.get(user=request.user)

        # TODO Objective 9: query for posts (HINT only return posts needed to be displayed)
        posts = models.Post.objects.all().order_by('-timestamp')
        posts_displayed = posts[:request.session.get('post_counter', 1)]

        # TODO Objective 10: check if user has like post, attach as a new attribute to each post

        context = { 'user_info' : user_info
                  , 'posts' : posts_displayed }
        return render(request,'messages.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')

def account_view(request):
    """Private Page Only an Authorized User Can View, allows user to update
       their account information (i.e UserInfo fields), including changing
       their password
    Parameters
    ---------
      request: (HttpRequest) should be either a GET or POST
    Returns
    --------
      out: (HttpResponse)
                 GET - if user is authenticated, will render account.djhtml
                 POST - handle form submissions for changing password, or User Info
                        (if handled in this view)
    """
        # TODO Objective 3: Create Forms and Handle POST to Update UserInfo / Password
    if request.user.is_authenticated:
        user_info = models.UserInfo.objects.get(user=request.user)

        # Password Change Form
        if request.method == "POST":
            change_pass_form = PasswordChangeForm(request.user, request.POST)
            if change_pass_form.is_valid():
                user = change_pass_form.save()
                update_session_auth_hash(request, user)
                logout(request)
                return redirect('login:login_view')
        else:
            change_pass_form = PasswordChangeForm(request.user)

        # User Info Update
        user_info_update_form = forms.UpdateForm()
    
        context = { 'user_info' : user_info,
                    'change_pass_form' : change_pass_form,
                    'user_info_update_form' : user_info_update_form
                }
        return render(request,'account.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')

def update_view(request):
    user_info = models.UserInfo.objects.get(user=request.user)

    # Update user information
    if request.method == "POST":
        user_info_update_form = forms.UpdateForm(request.POST)
        if user_info_update_form.is_valid():
            employment = user_info_update_form.cleaned_data['employment']
            location = user_info_update_form.cleaned_data['location']
            birthday = user_info_update_form.cleaned_data['birthday']
            new_interest = user_info_update_form.cleaned_data['interests']
            user_info.employment = employment
            user_info.location = location
            user_info.birthday = birthday
            user_info.interests.add(new_interest)
            user_info.save()
            return redirect('social:messages_view')

def people_view(request):
    """Private Page Only an Authorized User Can View, renders people page
       Displays all users who are not friends of the current user and friend requests
    Parameters
    ---------
      request: (HttpRequest) - should contain an authorized user
    Returns
    --------
      out: (HttpResponse) - if user is authenticated, will render people.djhtml
    """
    if request.user.is_authenticated:
        user_info = models.UserInfo.objects.get(user=request.user)
        # TODO Objective 4: create a list of all users who aren't friends to the current user (and limit size)
        all_people = list(models.UserInfo.objects.exclude(friends=user_info).exclude(user__username=user_info.user.username))

        # delete users that are requested to be friend from the current logged in user from the list
        # for fr_req in models.FriendRequest.objects.filter(from_user=user_info):
        #     all_people.remove(fr_req.to_user)

        all_people_display = all_people[:request.session.get('counter', 1)]

        # create a list of all people whom the current logged in user sent friend request to (for Objective 5)
        friend_requests_from_user_info = []
        fr_requests_from_user_info = models.FriendRequest.objects.filter(from_user=user_info)
        for fr_req in fr_requests_from_user_info:
            friend_requests_from_user_info.append(fr_req.to_user)

        # TODO Objective 5: create a list of all friend requests to current user
        friend_requests = list(models.FriendRequest.objects.filter(to_user=user_info))

        context = { 'user_info' : user_info,
                    'all_people' : all_people_display,
                    'friend_requests' : friend_requests,
                    'friend_requests_from_user_info' : friend_requests_from_user_info }

        return render(request,'people.djhtml',context)

    request.session['failed'] = True
    return redirect('login:login_view')

def like_view(request):
    '''Handles POST Request recieved from clicking Like button in messages.djhtml,
       sent by messages.js, by updating the corrresponding entry in the Post Model
       by adding user to its likes field
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute postID,
                                a string of format post-n where n is an id in the
                                Post model

	Returns
	-------
   	  out : (HttpResponse) - queries the Post model for the corresponding postID, and
                             adds the current user to the likes attribute, then returns
                             an empty HttpResponse, 404 if any error occurs
    '''
    postIDReq = request.POST.get('postID')
    if postIDReq is not None:
        # remove 'post-' from postID and convert to int
        # TODO Objective 10: parse post id from postIDReq
        postID = int(postIDReq[5:])

        if request.user.is_authenticated:
            # TODO Objective 10: update Post model entry to add user to likes field

            # get the current user object
            user_info = models.UserInfo.objects.get(user=request.user)

            # get the Post object with the corresponding id
            post = models.Post.objects.get(id=postID)
            # add current user to the list of people who likes the post
            post.likes.add(user_info)

            # return status='success'
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('like_view called without postID in POST')

def post_submit_view(request):
    '''Handles POST Request recieved from submitting a post in messages.djhtml by adding an entry
       to the Post Model
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute postContent, a string of content

	Returns
	-------
   	  out : (HttpResponse) - after adding a new entry to the POST model, returns an empty HttpResponse,
                             or 404 if any error occurs
    '''
    postContent = request.POST.get('postContent')
    print(postContent)
    if postContent is not None:
        if request.user.is_authenticated:

            # TODO Objective 8: Add a new entry to the Post model
            user_info = models.UserInfo.objects.get(user=request.user)
            models.Post.objects.create(owner=user_info, content=postContent)
            # return status='success'
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('post_submit_view called without postContent in POST')

def more_post_view(request):
    '''Handles POST Request requesting to increase the amount of Post's displayed in messages.djhtml
    Parameters
	----------
	  request : (HttpRequest) - should be an empty POST

	Returns
	-------
   	  out : (HttpResponse) - should return an empty HttpResponse after updating hte num_posts sessions variable
    '''
    if request.user.is_authenticated:
        # update the # of posts displayed

        # TODO Objective 9: update how many posts are displayed/returned by messages_view
        count = request.session.get('post_counter', 1)
        request.session['post_counter'] = count+2

        # return status='success'
        return HttpResponse()

    return redirect('login:login_view')

def more_ppl_view(request):
    '''Handles POST Request requesting to increase the amount of People displayed in people.djhtml
    Parameters
	----------
	  request : (HttpRequest) - should be an empty POST

	Returns
	-------
   	  out : (HttpResponse) - should return an empty HttpResponse after updating the num ppl sessions variable
    '''
    if request.user.is_authenticated:
        # update the # of people displayed

        # TODO Objective 4: increment session variable for keeping track of num ppl displayed
        i = request.session.get('counter', 1)
        request.session['counter'] = i+1
        # return status='success'
        return HttpResponse()

    return redirect('login:login_view')

def friend_request_view(request):
    '''Handles POST Request recieved from clicking Friend Request button in people.djhtml,
       sent by people.js, by adding an entry to the FriendRequest Model
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute frID,
                                a string of format fr-name where name is a valid username

	Returns
	-------
   	  out : (HttpResponse) - adds an etnry to the FriendRequest Model, then returns
                             an empty HttpResponse, 404 if POST data doesn't contain frID
    '''
    frID = request.POST.get('frID')
    if frID is not None:
        # remove 'fr-' from frID
        fr_requested_username = frID[3:]

        if request.user.is_authenticated:
            # TODO Objective 5: add new entry to FriendRequest
            current_user = models.UserInfo.objects.get(user=request.user)
            fr_requested_user = models.UserInfo.objects.get(user__username=fr_requested_username)
            models.FriendRequest.objects.create(to_user=fr_requested_user, from_user=current_user)

            # return status='success'
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('friend_request_view called without frID in POST')

def accept_decline_view(request):
    '''Handles POST Request recieved from accepting or declining a friend request in people.djhtml,
       sent by people.js, deletes corresponding FriendRequest entry and adds to users friends relation
       if accepted
    Parameters
	----------
	  request : (HttpRequest) - should contain json data with attribute decision,
                                a string of format A-name or D-name where name is
                                a valid username (the user who sent the request)

	Returns
	-------
   	  out : (HttpResponse) - deletes entry to FriendRequest table, appends friends in UserInfo Models,
                             then returns an empty HttpResponse, 404 if POST data doesn't contain decision
    '''
    data = request.POST.get('decision')
    if data is not None:
        # TODO Objective 6: parse decision from data
        AorD = data[:1]
        username = data[2:]

        if request.user.is_authenticated:

            # TODO Objective 6: delete FriendRequest entry and update friends in both Users
            current_user = models.UserInfo.objects.get(user=request.user)
            req_fr_user = models.UserInfo.objects.get(user__username=username)

            if AorD == 'A':
                current_user.friends.add(req_fr_user)
                
            models.FriendRequest.objects.filter(to_user=current_user, from_user=req_fr_user).delete()
            
            # return status='success'
            return HttpResponse()
        else:
            return redirect('login:login_view')

    return HttpResponseNotFound('accept-decline-view called without decision in POST')
