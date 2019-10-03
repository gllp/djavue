from core.models import User
from django.test.client import Client
from django.test.testcases import TestCase
from core.tests import fixtures
import json

QUESTION_EINSTEIN = 'What is E=mc²?'
QUESTION_JACKSON = 'Why? Why? Tell them that\'s human nature. Is it true?'
QUESTION_GEORGE = 'Where are all the good songs nowadays?'
ANSWER_JACKSON_TO_EINSTEIN = 'E = mc², equation in German-born physicist Albert Einstein’s theory of special ' \
                             'relativity that expresses the fact that mass and energy are the same physical entity ' \
                             'and can be changed into each other. In the equation, the increased relativistic ' \
                             'mass (m) of a body times the speed of light squared (c2) is equal to the kinetic ' \
                             'energy (E) of that body.'
ANSWER_GEORGE_TO_EINSTEIN = 'In physics, mass–energy equivalence states that anything having mass has an equivalent ' \
                            'amount of energy and vice versa, with these fundamental quantities directly relating to' \
                            ' one another by Albert Einstein\'s famous formula E=mc². This formula states that the' \
                            ' equivalent energy (E) can be calculated as the mass (m) multiplied by the speed of ' \
                            'light (c = ~3×108 m/s) squared. Similarly, anything having energy exhibits a ' \
                            'corresponding mass m given by its energy E divided by the speed of light squared c2.' \
                            ' Because the speed of light is a very large number in everyday units, the formula ' \
                            'implies that even an everyday object at rest with a modest amount of mass has a very' \
                            ' large amount of energy intrinsically. Chemical reactions, nuclear reactions, and other' \
                            ' energy transformations may cause a system to lose some of its energy content (and thus' \
                            ' some corresponding mass), releasing it as the radiant energy of light or as thermal' \
                            ' energy for example.'


class TestQuoraCloneApi(TestCase):
    @classmethod
    def setUpTestData(cls):
        fixtures.quoraclone_users()

    def test_quoraclone_api(self):
        einstein, jackson, george, anon = Client(), Client(), Client(), Client()
        einstein.force_login(User.objects.get(username='alberteinstein'))
        jackson.force_login(User.objects.get(username='mjackson'))
        george.force_login(User.objects.get(username='gmichael'))
        self._follow(einstein, 'gmichael')
        self._follow(einstein, 'mjackson')
        self._follow(jackson, 'gmichael')
        self._follow(jackson, 'alberteinstein')
        self._unfollow(einstein, 'mjackson')
        self._post_question(einstein, QUESTION_EINSTEIN)
        self._post_question(jackson, QUESTION_JACKSON)
        self._post_question(george, QUESTION_GEORGE)
        self._answer_question(jackson, QUESTION_EINSTEIN, 'alberteinstein', ANSWER_JACKSON_TO_EINSTEIN)
        self._follow(george, 'alberteinstein')
        self._answer_question(george, QUESTION_EINSTEIN, 'alberteinstein', ANSWER_GEORGE_TO_EINSTEIN)
        self._unfollow(george, 'alberteinstein')
        self._assert_question_home(george, [QUESTION_GEORGE])
        self._assert_question_home(einstein, [QUESTION_GEORGE, QUESTION_EINSTEIN])
        self._assert_question_home(jackson, [QUESTION_GEORGE, QUESTION_JACKSON, QUESTION_EINSTEIN])
        self._assert_question_home(anon, [QUESTION_GEORGE, QUESTION_JACKSON, QUESTION_EINSTEIN])
        self._assert_question_home_user(anon, 'alberteinstein', [QUESTION_EINSTEIN])
        self._assert_question_home_user(einstein, 'alberteinstein', [QUESTION_EINSTEIN])
        self._assert_question_page(jackson, 'alberteinstein', QUESTION_EINSTEIN, [ANSWER_GEORGE_TO_EINSTEIN,
                                                                                  ANSWER_JACKSON_TO_EINSTEIN])
        self._assert_question_page(jackson, 'gmichael', QUESTION_GEORGE, [])

    def _follow(self, client, username):
        c = client.post('/api/follow', {'username': username})
        self.assertEquals(200, c.status_code)
        data = json.loads(c.content.decode('utf-8'))
        self.assertIsNotNone(data)

    def _unfollow(self, client, username):
        c = client.post('/api/unfollow', {'username': username})
        self.assertEquals(200, c.status_code)
        data = json.loads(c.content.decode('utf-8'))
        self.assertIsNotNone(data)

    def _post_question(self, client, text):
        c = client.post('/api/post_question', {'text': text})
        self.assertEquals(200, c.status_code)
        new_question = json.loads(c.content.decode('utf-8'))
        self.assertIsNotNone(new_question['question']['id'])
        self.assertEquals(text, new_question['question']['title'])
        self.assertIsNotNone(new_question['details']['username'])

    def _answer_question(self, client, question_title, author_username, text):
        c = client.post('/api/post_answer', {'question_title': question_title, 'author_username': author_username,
                                             'text': text})
        self.assertEquals(200, c.status_code)
        new_answer = json.loads(c.content.decode('utf-8'))
        self.assertIsNotNone(new_answer['answer']['id'])
        self.assertEquals(text, new_answer['answer']['text'])
        self.assertIsNotNone(new_answer['details']['username'])

    def _assert_question_home(self, client, questions_list):
        c = client.get('/api/list_questions')
        self.assertEquals(200, c.status_code)
        data = json.loads(c.content.decode('utf-8'))
        actual_questions_texts = [question_wrapper['question']['title'] for question_wrapper in data]
        self.assertEquals(questions_list, actual_questions_texts)

    def _assert_question_page(self, client, author_username, question_title, answers_list):
        c = client.get('/api/get_question', {'question_title': question_title, 'author_username': author_username})
        ans = client.get('/api/get_answers', {'question_title': question_title, 'author_username': author_username})
        self.assertEquals(200, c.status_code)
        self.assertEquals(200, c.status_code)
        data_question = json.loads(c.content.decode('utf-8'))
        data_answers = json.loads(ans.content.decode('utf-8'))
        actual_answers_texts = [answer_wrapper['answer']['text'] for answer_wrapper in data_answers]
        self.assertEquals(answers_list, actual_answers_texts)
        self.assertEquals(question_title, data_question['question']['title'])

    def _assert_question_home_user(self, client, username, questions_list):
        c = client.get('/api/list_questions', {'username': username})
        ans = client.get('/api/get_user_details', {'username': username})
        self.assertEquals(200, c.status_code)
        self.assertEquals(200, ans.status_code)
        data_c = json.loads(c.content.decode('utf-8'))
        data_ans = json.loads(ans.content.decode('utf-8'))
        actual_questions_texts = [question_wrapper['question']['title'] for question_wrapper in data_c]
        self.assertEquals(questions_list, actual_questions_texts)
        for key in ['username', 'avatar', 'description', 'ifollow']:
            self.assertIsNotNone(data_ans[key])
