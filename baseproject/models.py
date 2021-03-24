from django.db import models


class User(models.Model):
    name = models.CharField()
    achievements = ["achievement1", "achievement2"]

    def add_achievements(self, a):
        return json.dumps(a)

    def get_achievements(self):
        return json.loads(self.achievements)
