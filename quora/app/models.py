from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Questions(models.Model):
    title = models.CharField(verbose_name="Sorunuz", max_length=250)
    user_id = models.ForeignKey(User)

    class Meta:
        verbose_name_plural = "Sorular"

    def __str__(self):
        return self.title

class Answers(models.Model):
    context = RichTextField()
    #sub_answer = models.ForeignKey("Answers", related_name="subAnswer")
    question_id = models.ForeignKey(Questions, related_name="questionId")
    user_id = models.ForeignKey(User, related_name="userId")

    class Meta:
        verbose_name_plural = "Cevaplar"

    def __str__(self):
        return self.context

class UpDownVotesAnswer(models.Model):
    up_down = models.BooleanField()
    answer_id = models.ForeignKey(Answers)
    user_id = models.ForeignKey(User, related_name="UDAUser")

    class Meta:
        verbose_name_plural = "UpDown Cevaplar"


class UpDownVotesQuestion(models.Model):
    up_down = models.BooleanField()
    question_id = models.ForeignKey(Questions)
    user_id = models.ForeignKey(User, related_name="UDQUser")
    
    class Meta:
        verbose_name_plural = "UpDown Sorular"

class SubAnswers(models.Model):
    answer_id = models.ForeignKey(Answers, related_name="realAnswer")
    subanswer_id = models.ForeignKey(Answers, related_name="subAnswer")

    class Meta:
        verbose_name_plural = "Alt Cevaplar"
    
    def __str__(self):
        return self.subanswer_id.context