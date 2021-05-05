"""
*  REFERENCES
*
*  Title: Testing Tools
*  Author: Django
*  URL: https://docs.djangoproject.com/en/3.2/topics/testing/tools/
*  
*  Title: How should I write tests from Forms in Django?
*  Author: Torsten Engelbrecht
*  URL: https://stackoverflow.com/questions/7304248/how-should-i-write-tests-for-forms-in-django
*
*  Title: Advanced testing topics
*  Author: Django
*  URL: https://docs.djangoproject.com/en/3.2/topics/testing/advanced/#methods
"""
from django.test import TestCase, Client, RequestFactory
from fitapp.models import User, Logs, Profile, Comment
from django.contrib.auth.models import User
import fitapp.views as views
from fitapp.forms import LogsForm, CommentForm
from fitapp.views import ProgressBar, LogReq, viewLogs, Achievements, leaderboard, update, updatelogs, userLogs, log, post_detail, deleteLog, shareable

# Create your tests here.
class DummyTestCase(TestCase):
    def setUp(self):
        x = 1
        self.logs_1 = Logs.objects.create(exercise="running", date="2021-04-11", duration="30", intensity="moderate", area="legs")
        self.comments_1 = Comment.objects.create(name="test", post=self.logs_1, body="test", created_on="2021-04-11", active=True)
        self.c = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='test', email='test@...', password='test')

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
        self.assertEqual(Test.post("/fitapp/Logs/", data={"exercise": "running", "date": "2021-04-11", "duration": "30", "intensity": "moderate", "area": "legs"}).status_code, 200)
    
    def test_commentsform(self):
        form_data={'name': 'test', 'body': 'test'}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_commentsform2(self):
        form_data={'name': 'fjkfjdksflkdjfsdkjfldksjflfjdkslfdsfkjdslkfjdlsfkjkldsfjkdslfdkjsldfjsdlkjfdskjfldskfj', 'body': 'test'}
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_commentsform3(self):
        form_data={'name': '', 'body': 'test'}
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_profileviews(self):
        request = self.factory.get('/fitapp/progress/')
        request.user = self.user
        response = ProgressBar(request)
        self.assertEqual(response.status_code, 200)

    def test_logreqviews(self):
        request = self.factory.get('/fitapp/Logs/')
        request.user = self.user
        response = LogReq(request)
        self.assertEqual(response.status_code, 200)

    def test_viewlogsviews(self):
        request = self.factory.get('/fitapp/viewLogs/')
        request.user = self.user
        response = viewLogs(request)
        self.assertEqual(response.status_code, 200)

    def test_achievementsviews(self):
        request = self.factory.get('/fitapp/achievements/')
        request.user = self.user
        response = Achievements(request)
        self.assertEqual(response.status_code, 200)
    
    def test_leaderboardviews(self):
        request = self.factory.get('fitapp/leaderboard/')
        request.user = self.user
        response = leaderboard(request)
        self.assertEqual(response.status_code, 200)

    def test_updateviews(self):
        request = self.factory.get('fitapp/achievements/update/<int:user_id>/')
        request.user = self.user
        response = update(request, self.user.id)
        self.assertEqual(response.status_code, 200)

    def test_updatelogsviews(self):
        request = self.factory.get('fitapp/Logs/updatelogs/<int:user_id>')
        request.user = self.user
        response = updatelogs(request, self.user.id)
        self.assertEqual(response.status_code, 200)

    def test_userlogsviews(self):
        request = self.factory.get('fitapp/userLogs/<int:user_id>')
        request.user = self.user
        response = userLogs(request, self.user.id)
        self.assertEqual(response.status_code, 200) 

    def test_logviews(self):
        request = self.factory.get('viewLogs/<int:logs_id>')
        request.user = self.user
        response = log(request, self.logs_1.id)
        self.assertEqual(response.status_code, 200) 

    def test_postdetailviews(self):
        request = self.factory.get('viewLogs/<int:logs_id>/comment')
        request.user = self.user
        response = post_detail(request, self.logs_1.id)
        self.assertEqual(response.status_code, 200) 

    def test_deletelogsviews(self):
        request = self.factory.get('viewLogs/<int:logs_id>/deleteLog')
        request.user = self.user
        response = deleteLog(request, self.logs_1.id)
        self.assertEqual(response.status_code, 302) 

    def test_shareableviews(self):
        request = self.factory.get('viewLogs/<int:logs_id>/shareable')
        request.user = self.user
        response = shareable(request, self.logs_1.id)
        self.assertEqual(response.status_code, 200) 