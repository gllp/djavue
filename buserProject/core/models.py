from django.db import models
from django.contrib.auth.models import User
from commons.utils import gravatar_url
from datetime import datetime


class ActivityLog(models.Model):
    type = models.CharField(max_length=64)
    logged_user = models.ForeignKey(User, null=True, blank=True)
    fromuser = models.ForeignKey(User, null=True, blank=True, related_name="activitylogs_withfromuser")
    jsondata = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '%s / %s / %s' % (
            self.type,
            self.logged_user,
            self.created_at,
        )


class Todo(models.Model):
    description = models.CharField(max_length=512)
    done = models.BooleanField(default=False)

    def to_dict_json(self):
        return {
            'id': self.id,
            'description': self.description,
            'done': self.done,
        }


class Following(models.Model):
    follow_from = models.ForeignKey(User, related_name="following_from")
    follow_to = models.ForeignKey(User, related_name="following_to")

    class Meta:
        unique_together = ['follow_from', 'follow_to']


class Question(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'title']
        ordering = ('-created_at',)

    def to_dict_json(self):
        return {
            'id': self.id,
            'author_name': self.user.first_name,
            'author_username': self.user.username,
            'create_at': self.created_at.isoformat(),
            'title': self.title,
        }


class Answer(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=2048)

    def to_dict_json(self):
        return {
            'id': self.id,
            'author_name': self.user.first_name,
            'author_username': self.user.username,
            'text': self.text,
        }


class UserExtraInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="user_extra")
    description = models.CharField(max_length=512)
    avatar_email = models.CharField(max_length=2048)

    def to_dict_json(self, ifollow):
        return {
            'username': self.user.username,
            'description': self.description,
            'avatar': gravatar_url(self.avatar_email),
            'ifollow': ifollow if ifollow else False,
        }
