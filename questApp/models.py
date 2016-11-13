from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    """Вопрос или тема для обсуждения"""
    text = models.CharField(verbose_name="Вопрос", max_length=200)
    date_added = models.DateTimeField(verbose_name="Дата добавления вопроса", auto_now_add=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.text

    class Meta:
        ordering = ('date_added',)
        verbose_name_plural = 'Вопросы'

class Answer(models.Model):
    """Ответ на вопрос"""
    question = models.ForeignKey(Question)
    text = models.TextField(verbose_name="Ответ")
    date_added = models.DateTimeField(verbose_name="Дата добавления ответа", auto_now_add=True)

    class Meta:
        verbose_name_plural = "Ответы"

    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.text[:50] + "..."


