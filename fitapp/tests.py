from django.test import TestCase
from fitapp.models import User, Logs
from django.contrib.auth.models import User
import fitapp.views as views

# Create your tests here.
class DummyTestCase(TestCase):
    def setUp(self):
        x = 1
        self.logs_1 = Logs.objects.create(exercise="running", date="4/5/2021", duration="30 minutes", intensity="medium", area="legs")

    def test_dummy_test_case(self):
        # self.assertEqual(1, 1)
        Test = self.logs_1
        print(Test.__str__())
        self.assertEqual(Test.__str__(), "4/5/2021" + ":" + "running" + "\n")
