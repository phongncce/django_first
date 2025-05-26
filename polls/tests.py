import datetime

from django.test import TestCase
from django.utils import timezone

from polls.models import Question


# Create your tests here.
class QuestionModelTest(TestCase):
    def test_was_recent_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=5)
        future_question = Question(create_date=time)

        self.assertIs(future_question.was_recent(), False)

    def test_was_recent_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(create_date=time)

        self.assertIs(old_question.was_recent(), False)

    def test_was_recent_with_recent_question(self):
        time2 = timezone.now() - datetime.timedelta(days=1, seconds=-5)
        time3 = timezone.now() - datetime.timedelta(seconds=1)

        recent_question = Question(create_date=time2)
        self.assertIs(recent_question.was_recent(), True)
        recent_question = Question(create_date=time3)
        self.assertIs(recent_question.was_recent(), True)
