from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(unique=True, max_length=250)

    def __unicode__(self):
        return self.username


class HistPassword(models.Model):
    user = models.ForeignKey(User)
    password = models.CharField(max_length=250)
    date_change = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return '%s' % (self.password)
