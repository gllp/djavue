from core.models import User, Following, UserExtraInfo
from django.db.models import Q

custom_avatar = 'https://encrypted-tbn0.gstatic.com/images?q=tbn' \
                '%3AANd9GcR91699RiTL8B1dWszZ9xt6dRrv3meTTP_oeNDC1Y4ESGCueEPg '


def get_user_details(request_user, username):
    page_user = User.objects.get(username=username)
    ifollow = False
    if request_user is not None:
        ifollow = Following.objects.filter(follow_from=request_user, follow_to=page_user).count() > 0
    if UserExtraInfo.objects.filter(user=page_user).count() == 0:
        return {'username': username, 'avatar': custom_avatar, 'description': '', 'ifollow': ifollow}
    details = UserExtraInfo.objects.get(user=page_user)
    return details.to_dict_json(ifollow)


def get_users_list(request_user, username):
    if request_user is not None:
        user_details = UserExtraInfo.objects.filter(~Q(user=request_user))
    else:
        user_details = UserExtraInfo.objects.all()
    return [user_detail.to_dict_json(False) for user_detail in user_details]


def post_new_user(user):
    if User.objects.filter(Q(username=user['username']) | Q(email=user['email'])).count() > 0:
        return {}
    new_user = User.objects.create_user(username=user['username'], email=user['email'], password=user['password'])
    new_user.first_name = user['first_name']
    new_user.last_name = user['last_name']
    new_user.save()
    UserExtraInfo.objects.create(user=new_user, description=user['description'], avatar_email=user['email'])
    return user


def get_profile(username):
    user = User.objects.get(username=username)
    extrainfo = {'username': username, 'description': '', 'avatar_email': '', 'ifollow': False}
    if UserExtraInfo.objects.filter(user=user).count() > 0:
        extrainfo = UserExtraInfo.objects.get(user=user).to_dict_json(False)
    return {'first_name': user.first_name, 'username': username, 'email': user.email, 'description': extrainfo['description']}