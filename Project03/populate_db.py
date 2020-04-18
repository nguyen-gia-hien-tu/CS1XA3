from social import models

def populate():
    # Populate UserInfo table
    models.UserInfo.objects.create_user_info(username="Alex Johnson", password="JAx#10o1")