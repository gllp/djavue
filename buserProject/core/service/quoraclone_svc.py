from core.models import User, Following, Question, Answer


def follow(user, username):
    user_from = User.objects.get(username=username)
    if Following.objects.filter(follow_from=user, follow_to=user_from).count() == 0:
        Following.objects.create(follow_from=user, follow_to=user_from)


def unfollow(user, username):
    user_from = User.objects.get(username=username)
    Following.objects.filter(follow_from=user, follow_to=user_from).delete()


def post_question(user, text):
    Question.objects.create(user=user, title=text)


def post_answer(user, question_title, question_author, text):
    author = User.objects.get(username=question_author)
    question = Question.objects.get(title=question_title, user=author)
    Answer.objects.create(user=user, question=question, text=text)


def list_questions(user, username):
    if username:
        questions = Question.objects.filter(user__username=username)
    else:
        if user is not None:
            questions = Question.objects.filter(user__in=User.objects.filter(following_to__follow_from=user))
        else:
            questions = Question.objects.all()
    return [question.to_dict_json() for question in questions]


def get_question(question_title, question_author):
    user = User.objects.get(username=question_author)
    question = Question.objects.get(title=question_title, user=user)
    return question.to_dict_json()


def get_answers(question_title, question_author):
    user = User.objects.get(username=question_author)
    answers = Answer.objects.filter(question=Question.objects.get(title=question_title, user=user))
    return [answer.to_dict_json() for answer in answers]
