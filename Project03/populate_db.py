from social import models

import datetime

def populate():
    # Populate users table
    models.UserInfo.objects.create_user_info(username="Alex Johnson", password="JAx#10o1")
    models.UserInfo.objects.create_user_info(username="Bethany Isokov", password="bEv$99oO")
    models.UserInfo.objects.create_user_info(username="Cathy Liang", password="litC!10")
    models.UserInfo.objects.create_user_info(username="Denise Song", password="EeLyn!02")
    models.UserInfo.objects.create_user_info(username="Emerald Diamond", password="10000$diamoND")
    models.UserInfo.objects.create_user_info(username="Fang Cao", password="HacKTh3$0vtH")
    models.UserInfo.objects.create_user_info(username="General Major", password="123$tanDUP")
    models.UserInfo.objects.create_user_info(username="Henry Tu", password="hIeenGiv#04o1")
    models.UserInfo.objects.create_user_info(username="India Northway", password="inLin$04")
    models.UserInfo.objects.create_user_info(username="Jafar Evil", password="HahaHaaaaa$01")
    
    ## Accidentally created too many users and don't want to delete them :(((
    # models.UserInfo.objects.create_user_info(username="Kathy Zhao", password="zKaY&o57")
    # models.UserInfo.objects.create_user_info(username="Lindy Xin", password="XiN1La$")
    # models.UserInfo.objects.create_user_info(username="Mandy Wong", password="Doc$tranG3")
    # models.UserInfo.objects.create_user_info(username="Nani What", password="WhatTh3F**$")
    # models.UserInfo.objects.create_user_info(username="Ortho Gornal", password="d0tProDI$0")
    # models.UserInfo.objects.create_user_info(username="Perry Plat", password="PhinF3rB2")
    # models.UserInfo.objects.create_user_info(username="Quinn Stacy", password="Pr3tt$09")
    # models.UserInfo.objects.create_user_info(username="Ron Johnson", password="Jr.0oNson$")
    # models.UserInfo.objects.create_user_info(username="Steven Nice", password="$NiC3ooK0")
    # models.UserInfo.objects.create_user_info(username="Terry Li", password="FfoRr3$pec")
    # models.UserInfo.objects.create_user_info(username="Ubuntu Oscar", password="hacK3RFor$")
    # models.UserInfo.objects.create_user_info(username="Vivian Ying", password="Ch1nV$I09")
    # models.UserInfo.objects.create_user_info(username="Wander Yonder", password="H3YHh0QuaO$")
    # models.UserInfo.objects.create_user_info(username="Xander Nguyen", password="NGinX$8sT")
    # models.UserInfo.objects.create_user_info(username="Ying Yang", password="5$5FivEvI")
    # models.UserInfo.objects.create_user_info(username="Zen Ren", password="$3xY6Ir1S")

    # Create Interest objects
    aerobics      = models.Interest.objects.create(label="Aerobics")
    baking        = models.Interest.objects.create(label="Baking")
    baseball      = models.Interest.objects.create(label="Baseball")
    basketball    = models.Interest.objects.create(label="Basketball")
    bird_watching = models.Interest.objects.create(label="Birdwatching")
    blogging      = models.Interest.objects.create(label="Blogging")
    bowling       = models.Interest.objects.create(label="Bowling")
    board_game    = models.Interest.objects.create(label="Board Game")
    chess         = models.Interest.objects.create(label="Playing Chess")
    coding        = models.Interest.objects.create(label="Coding")
    collecting    = models.Interest.objects.create(label="Collecting")
    cooking       = models.Interest.objects.create(label="Cooking")
    dancing       = models.Interest.objects.create(label="Dancing")
    drawing       = models.Interest.objects.create(label="Drawing")
    eating        = models.Interest.objects.create(label="Eating")
    gaming        = models.Interest.objects.create(label="Playing Video Games")
    gardening     = models.Interest.objects.create(label="Gardening")
    gym           = models.Interest.objects.create(label="Gymnastic")    
    watching      = models.Interest.objects.create(label="Watching TV")
    netfilx       = models.Interest.objects.create(label="Netflix and Chill")
    karate        = models.Interest.objects.create(label="Karate")
    reading       = models.Interest.objects.create(label="Reading")
    magic         = models.Interest.objects.create(label="Doing magic trick")
    pokemon       = models.Interest.objects.create(label="Playing Pokemon Go")

    # Create UserInfo for some users
    alex = models.UserInfo.objects.get(user__username="Alex Johnson")
    bethany = models.UserInfo.objects.get(user__username="Bethany Isokov")
    cathy = models.UserInfo.objects.get(user__username="Cathy Liang")
    denise = models.UserInfo.objects.get(user__username="Denise Song")
    emerald = models.UserInfo.objects.get(user__username="Emerald Diamond")
    fang = models.UserInfo.objects.get(user__username="Fang Cao")
    general = models.UserInfo.objects.get(user__username="General Major")
    henry = models.UserInfo.objects.get(user__username="Henry Tu")
    india = models.UserInfo.objects.get(user__username="India Northway")
    jafar = models.UserInfo.objects.get(user__username="Jafar Evil")

    alex.employment = "Student"
    alex.location = "Toronto, ON, Canada"
    alex.birthday = datetime.date(2000, 2, 18)
    alex.interests.add(cooking, dancing, netfilx, eating)
    alex.friends.add(cathy, denise, india)
    alex.save()

    bethany.employment = "Cashier"
    bethany.location = "Ottawa, ON, Canada"
    bethany.birthday = datetime.date(1997, 8, 10)
    bethany.interests.add(karate, gym, watching)
    bethany.friends.add(fang, general, jafar, denise)
    bethany.save()

    cathy.employment = "Architecture"
    cathy.location = "Vancouver, BC, Canada"
    cathy.birthday = datetime.date(1998, 9, 1)
    cathy.interests.add(board_game, bowling)
    cathy.friends.add(alex, jafar, henry, india)
    cathy.save()

    denise.employment = "Actress"
    denise.location = "Waterloo, ON, Canada"
    denise.birthday = datetime.date(1990, 10, 15)
    denise.interests.add(baking, coding, drawing)
    denise.friends.add(alex, bethany, india, emerald, fang, henry)
    denise.save()

    emerald.employment = "Youtuber"
    emerald.location = "Montreal, QB, Canada"
    emerald.birthday = datetime.date(1990, 8, 12)
    emerald.interests.add(baseball, basketball, bowling)
    emerald.friends.add(denise, jafar)
    emerald.save()

    fang.employment = "Ethical Hacker"
    fang.location = "Vancouver, BC, Canada"
    fang.birthday = datetime.date(2001, 12, 21)
    fang.interests.add(coding, gaming)
    fang.friends.add(bethany, denise, general, henry)
    fang.save()

    general.employment = "General"
    general.location = "Hamilton, ON, Canada"
    general.birthday = datetime.date(1980, 10, 12)
    general.interests.add(reading)
    general.friends.add(fang, bethany)
    general.save()
    
    henry.employment = "Student"
    henry.location = "Hamilton, ON, Canada"
    henry.birthday = datetime.date(2001, 6, 19)
    henry.interests.add(coding, watching, board_game)
    henry.friends.add(india, fang, cathy, denise)
    henry.save()

    india.employment = "Student"
    india.location = "Cambridge, ON, Canada"
    india.birthday = datetime.date(2000, 8, 16)
    india.interests.add(reading, blogging)
    india.friends.add(alex, henry, cathy, denise)
    india.save()

    jafar.employment = "Magician"
    jafar.location = "Beyond the Earth"
    jafar.birthday = datetime.date(1222, 12, 12)
    jafar.interests.add(magic)
    jafar.friends.add(bethany, cathy, emerald)
    jafar.save()

    # Create Post table
    post1 = models.Post.objects.create(owner=alex, content="Hi, how are you guys?")
    post1.likes.add(alex, denise, fang, henry)

    post2 = models.Post.objects.create(owner=fang, content="Welcome to the world of HaK3R")
    post2.likes.add(fang)

    post3 = models.Post.objects.create(owner=india, content="Wowwwww")
    post3.likes.add(fang, india)
    
    post4 = models.Post.objects.create(owner=denise, content="Stay Healthy guys!!!")
    post4.likes.add(denise, fang, india, henry, alex, bethany, cathy, emerald)
    
    post5 = models.Post.objects.create(owner=cathy, content="Posting my first post")
    post5.likes.add(henry, fang, cathy, jafar)

    post6 = models.Post.objects.create(owner=emerald, content="Hello There!")
    post6.likes.add(emerald, cathy, bethany)

    post7 = models.Post.objects.create(owner=general, content="Shoutout to all the front line workers out there!")
    post7.likes.add(general, fang, cathy, bethany, henry, india)

    # Create FriendRequest table
    fr_req_1 = models.FriendRequest.objects.create(to_user=denise, from_user=jafar)
    fr_req_2 = models.FriendRequest.objects.create(to_user=henry, from_user=alex)
    fr_req_3 = models.FriendRequest.objects.create(to_user=general, from_user=denise)
    fr_req_4 = models.FriendRequest.objects.create(to_user=india, from_user=emerald)
    fr_req_5 = models.FriendRequest.objects.create(to_user=alex, from_user=bethany)
    fr_req_6 = models.FriendRequest.objects.create(to_user=henry, from_user=emerald)
    fr_req_7 = models.FriendRequest.objects.create(to_user=henry, from_user=bethany)