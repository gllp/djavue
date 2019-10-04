from core.models import User, Following, Question, Answer
from core.service import user_svc
from django.db.models import Q


def follow(user, username):
    user_from = User.objects.get(username=username)
    if Following.objects.filter(follow_from=user, follow_to=user_from).count() == 0:
        Following.objects.create(follow_from=user, follow_to=user_from)


def unfollow(user, username):
    user_from = User.objects.get(username=username)
    Following.objects.filter(follow_from=user, follow_to=user_from).delete()


def post_question(user, text):
    Question.objects.create(user=user, title=text)
    question = Question.objects.get(user=user, title=text)
    return {'question': question.to_dict_json(), 'details': user_svc.get_user_details(user, user.username)}


def post_answer(user, question_title, question_author, text):
    author = User.objects.get(username=question_author)
    question = Question.objects.get(title=question_title, user=author)
    Answer.objects.create(user=user, question=question, text=text)
    answer = Answer.objects.get(user=user, question=question, text=text)
    return {'answer': answer.to_dict_json(), 'details': user_svc.get_user_details(user, user.username)}


def list_questions(user, username):
    if username:
        questions = Question.objects.filter(user__username=username)
    else:
        if user is not None:
            questions = Question.objects.filter(Q(user__in=User.objects.filter(following_to__follow_from=user))
                                                | Q(user=user))
        else:
            questions = Question.objects.all()
    return [{'question': question.to_dict_json(), 'details': user_svc.get_user_details(user, question.user.username)}
            for question in questions]


def get_question(request_user, question_title, question_author):
    user = User.objects.get(username=question_author)
    question = Question.objects.get(title=question_title, user=user)
    return {'question': question.to_dict_json(), 'details': user_svc.get_user_details(request_user
                                                                                      , question.user.username)}


def get_answers(request_user, question_title, question_author):
    user = User.objects.get(username=question_author)
    answers = Answer.objects.filter(question=Question.objects.get(title=question_title, user=user))
    return [{'answer': answer.to_dict_json(), 'details': user_svc.get_user_details(request_user, answer.user.username)}
            for answer in answers]
