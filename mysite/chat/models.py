from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Member(models.Model):
    username = models.CharField(max_length=100)
    def __str__(self):
        return self.username.capitalize()

class SuggestionModel(models.Model):
    suggestion = models.CharField(
        max_length=240
    )
    answers = models.CharField(
        max_length=240
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.id) + " " + str(self.author.username) + " " + self.suggestion + " " + self.answers

class CommentModel(models.Model):
    comment = models.CharField(max_length=240)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    suggestion = models.ForeignKey(
        SuggestionModel,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.id) + " " + str(self.author.username) + " " + self.comment