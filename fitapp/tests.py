from django.test import TestCase
from fitapp.models import User, Logs
from django.contrib.auth.models import User
import fitapp.views as views

# Create your tests here.
class DummyTestCase(TestCase):
    def setUp(self):
        x = 1
        # self.user_1 = User.objects.create_user(username="test", email='test@gmail.com', password='test')
        # self.logs_1

    def test_dummy_test_case(self):
        self.assertEqual(1, 1)

    # def test_dummy_test_case(self):
    #     Test = User()
    #     Test.user = self.user_1
    #     print(Test.__str__())
    #     self.assertEqual(Test.__str__(), "test Profile")

