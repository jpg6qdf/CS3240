from django.test import TestCase
from fitapp.models import User, Logs, Profile
from django.contrib.auth.models import User
import fitapp.views as views

# Create your tests here.
class DummyTestCase(TestCase):
    def setUp(self):
        x = 1
        self.logs_1 = Logs.objects.create(exercise="running", date="2021-04-11", duration="30", intensity="moderate")
        testuser = User.objects.create(username="test10", email="test10@gmail.com")
        self.profile_1 = Profile.objects.create(user=testuser, level=5, current=65, maximum=100)


    def test_log(self):
        # self.assertEqual(1, 1)
        Test = self.logs_1
        print(Test.__str__())
        self.assertEqual(Test.__str__(), "2021-04-11" + ":" + "running" + "\n")

    def test_profile(self):
        Test = self.profile_1
        print(Test.__str__())
        self.assertEqual(Test.__str__(), "test10 Profile")
