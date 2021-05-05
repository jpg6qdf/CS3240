"""
*  REFERENCES
*
*  Title: Testing Tools
*  Author: Django
*  URL: https://docs.djangoproject.com/en/3.2/topics/testing/tools/
"""
from django.test import TestCase, Client
from fitapp.models import User, Logs, Profile, Comment
from django.contrib.auth.models import User
import fitapp.views as views
from fitapp.forms import LogsForm, CommentForm

# Create your tests here.
class DummyTestCase(TestCase):
    def setUp(self):
        x = 1
        p = Profile()
        self.logs_1 = Logs.objects.create(exercise="running", date="2021-04-11", duration="30", intensity="moderate", area="legs", owner=p)
        testuser = User.objects.create(username="test10", email="test10@gmail.com")
        self.comments_1 = Comment.objects.create(name="test", post=self.logs_1, body="test", created_on="2021-04-11", active=True)
        self.c = Client()

    def test_log(self):
        Test = self.logs_1
        print(Test.__str__())
        self.assertEqual(Test.__str__(), "2021-04-11" + ":" + "running" + "\n")

    def test_comment(self):
        Test = self.comments_1
        print(Test.__str__())
        self.assertEqual(Test.__str__(), "Comment test by test")

    def test_hometab_beforelogin(self):
        Test = self.c
        self.assertEqual(Test.get('/').status_code, 200)

    def test_profiletab_beforelogin(self):
        Test = self.c
        self.assertEqual(Test.get('/fitapp/progress/').status_code, 302)

    def test_logstab_beforelogin(self):
        Test = self.c
        self.assertEqual(Test.get('/fitapp/Logs/').status_code, 302)
    
    def test_viewlogstab_beforelogin(self):
        Test = self.c
        self.assertEqual(Test.get('/fitapp/viewLogs/').status_code, 302)

    def test_achievementstab_beforelogin(self):
        Test = self.c
        self.assertEqual(Test.get('/fitapp/achievements/').status_code, 302)

    def test_leaderboardtab_beforelogin(self):
        Test = self.c
        self.assertEqual(Test.get('/fitapp/leaderboard/').status_code, 302)

    def test_hometab_afterlogin(self):
        Test = self.c
        adminuser = User.objects.create_superuser(username="testadmin")
        Test.force_login(adminuser)
        self.assertEqual(Test.get('/').status_code, 200)
    
    def test_profiletab_afterlogin(self):
        Test = self.c
        adminuser = User.objects.create_superuser(username="testadmin")
        Test.force_login(adminuser)
        testprofile = Profile(user=adminuser)
        self.assertEqual(Test.get('/fitapp/progress/').status_code, 200)

    def test_logstab_afterlogin(self):
        Test = self.c
        adminuser = User.objects.create_superuser(username="testadmin")
        Test.force_login(adminuser)
        self.assertEqual(Test.get('/fitapp/Logs/').status_code, 200)

    def test_viewlogstab_afterlogin(self):
        Test = self.c
        adminuser = User.objects.create_superuser(username="testadmin")
        Test.force_login(adminuser)
        self.assertEqual(Test.get('/fitapp/viewLogs/').status_code, 200)

    def test_achievementstab_afterlogin(self):
        Test = self.c
        adminuser = User.objects.create_superuser(username="testadmin")
        Test.force_login(adminuser)
        self.assertEqual(Test.get('/fitapp/achievements/').status_code, 200)

    def test_leaderboard_afterlogin(self):
        Test = self.c
        adminuser = User.objects.create_superuser(username="testadmin")
        Test.force_login(adminuser)
        self.assertEqual(Test.get('/fitapp/leaderboard/').status_code, 200)
    
    def test_logstab_submitalog(self):
        Test = self.c
        adminuser = User.objects.create_superuser(username="testadmin")
        Test.force_login(adminuser)
        self.assertEqual(Test.post("/fitapp/Logs/", data={"exercise": "running", "date": "2021-04-11", "duration": "30", "intensity": "moderate"}).status_code, 200)

    # def test_logform(self):
    #     form_data = {"exercise": "running", "date": "2021-04-11", "duration": "30", "intensity": "moderate"}
    #     form = LogsForm(data=form_data)
    #     self.assertTrue(form.is_valid())
