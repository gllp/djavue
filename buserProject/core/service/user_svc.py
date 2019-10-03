from core.models import User, Following, Question, Answer, UserExtraInfo

custom_avatar = 'https://encrypted-tbn0.gstatic.com/images?q=tbn' \
                '%3AANd9GcR91699RiTL8B1dWszZ9xt6dRrv3meTTP_oeNDC1Y4ESGCueEPg '


def get_user_details(request_user, username):
    page_user = User.objects.get(username=username)
    ifollow = False
    if request_user is not None:
        ifollow = Following.objects.filter(follow_from=request_user, follow_to=page_user).count() > 0
    if UserExtraInfo.objects.filter(user=page_user).count() == 0:
        return {'username': username, 'avatar': custom_avatar, 'description': '', 'ifollow': ifollow}
    details = UserExtraInfo.objects.get(username=username)
    return details.to_dict_json(ifollow)
