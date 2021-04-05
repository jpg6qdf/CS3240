from django.test import TestCase
from fitapp.models import User, Logs
from django.contrib.auth.models import User

# Create your tests here.
class DummyTestCase(TestCase):
    def setUp(self):
        x = 1
        self.user_1 = User.objects.create_user(username="test", email='test@gmail.com', password='test')

    def test_dummy_test_case(self):
        Test = User()
        Test.user = self.user_1
        print(Test.__str__())
        self.assertEqual(Test.__str__(), "test Profile")

