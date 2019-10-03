# coding: utf-8
import json
from django.http.response import HttpResponse, JsonResponse
from django.contrib import auth
from commons.django_model_utils import get_or_none
from commons.django_views_utils import ajax_login_required
from core.service import log_svc, todo_svc, quoraclone_svc, user_svc
from django.views.decorators.csrf import csrf_exempt


def dapau(request):
    raise Exception('break on purpose')


@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    user_dict = None
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            log_svc.log_login(request.user)
            user_dict = _user2dict(user)
    return JsonResponse(user_dict, safe=False)


def logout(request):
    if request.method.lower() != 'post':
        raise Exception('Logout only via post')
    if request.user.is_authenticated():
        log_svc.log_logout(request.user)
    auth.logout(request)
    return HttpResponse('{}', content_type='application/json')


def whoami(request):
    i_am = {
        'user': _user2dict(request.user),
        'authenticated': True,
    } if request.user.is_authenticated() else {'authenticated': False}
    return JsonResponse(i_am)


@ajax_login_required
def add_todo(request):
    todo = todo_svc.add_todo(request.POST['new_task'])
    return JsonResponse(todo)


@ajax_login_required
def list_todos(request):
    todos = todo_svc.list_todos()
    return JsonResponse({'todos': todos})


def list_questions(request):
    user = request.user if request.user.is_authenticated() else None
    # Return NULL the .GET option if value not present
    username = request.GET.get('username')
    questions = quoraclone_svc.list_questions(user, username)
    return JsonResponse(questions, safe=False)


def get_question(request):
    user = request.user if request.user.is_authenticated() else None
    question_title = request.GET['question_title']
    question_author = request.GET['author_username']
    question = quoraclone_svc.get_question(user, question_title, question_author)
    return JsonResponse(question)


def get_answers(request):
    user = request.user if request.user.is_authenticated() else None
    question_title = request.GET['question_title']
    question_author = request.GET['author_username']
    answers = quoraclone_svc.get_answers(user, question_title, question_author)
    return JsonResponse(answers, safe=False)


def get_user_details(request):
    user = request.user if request.user.is_authenticated() else None
    username = request.GET.get('username')
    user_details = user_svc.get_user_details(user, username)
    return JsonResponse(user_details)


@ajax_login_required
def follow(request):
    username = request.POST['username']
    quoraclone_svc.follow(request.user, username)
    return JsonResponse({})


@ajax_login_required
def unfollow(request):
    username = request.POST['username']
    quoraclone_svc.unfollow(request.user, username)
    return JsonResponse({})


@ajax_login_required
def post_question(request):
    text = request.POST['text']
    question_wrapper = quoraclone_svc.post_question(request.user, text)
    return JsonResponse(question_wrapper)


@ajax_login_required
def post_answer(request):
    text = request.POST['text']
    question_title = request.POST['question_title']
    question_author = request.POST['author_username']
    new_answer = quoraclone_svc.post_answer(request.user, question_title, question_author, text)
    return JsonResponse(new_answer)


def _user2dict(user):
    d = {
        'id': user.id,
        'name': user.get_full_name(),
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'permissions': {
            'ADMIN': user.is_superuser,
            'STAFF': user.is_staff,
        }
    }
    return d
