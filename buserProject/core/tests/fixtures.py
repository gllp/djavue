from core.models import User, UserExtraInfo


def user_jon():
    ze = User.objects.create_user(
        username='jon',
        first_name='Jon',
        last_name='Snow',
        email='jon@example.com',
        password='snow',
    )
    return ze


def quoraclone_users():
    User.objects.create_user(username='alberteinstein')
    User.objects.create_user(username='mjackson')
    User.objects.create_user(username='gmichael')
    UserExtraInfo.objects.create(user=User.objects.get_by_natural_key(username='alberteinstein'),
                                 description='Fake Description',
                                 avatar_email='Fake_Mail')
    UserExtraInfo.objects.create(user=User.objects.get_by_natural_key(username='mjackson'),
                                 description='Fake Description',
                                 avatar_email='Fake_Mail')
    UserExtraInfo.objects.create(user=User.objects.get_by_natural_key(username='gmichael'),
                                 description='Fake Description',
                                 avatar_email='Fake_Mail')