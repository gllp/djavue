from core import views
from django.conf.urls import url

urlpatterns = [
    url(r'^api/dapau$', views.dapau),
    url(r'^api/login$', views.login),
    url(r'^api/logout$', views.logout),
    url(r'^api/whoami$', views.whoami),

    url(r'^api/add_todo$', views.add_todo),
    url(r'^api/list_todos$', views.list_todos),
    url(r'^api/list_questions$', views.list_questions),
    url(r'^api/follow$', views.follow),
    url(r'^api/unfollow$', views.unfollow),
    url(r'^api/post_question$', views.post_question),
    url(r'^api/post_answer$', views.post_answer),
    url(r'^api/get_question$', views.get_question),
    url(r'^api/get_answers$', views.get_answers),
    url(r'^api/get_user_details$', views.get_user_details),
    url(r'^api/users_list$', views.get_users_list),
]
