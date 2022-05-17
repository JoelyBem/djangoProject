from django.test import TestCase

from .models import Question
from django.utils import timezone
# Create your tests here.


class QuestionModelTests(TestCase):
	def test_was_published_recently_with_future_question(self):
		time = timezone.now()