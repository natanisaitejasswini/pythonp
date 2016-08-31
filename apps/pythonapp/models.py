from __future__ import unicode_literals
from ..loginapp.models import Userlog
from django.db import models
class Pokes(models.Model):
    user = models.ForeignKey('loginapp.Userlog', related_name="user1")
    userpoked = models.ForeignKey('loginapp.Userlog', related_name='user2')
    poked = models.IntegerField(default = "1")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)