from django.db import models


class Question(models.Model):

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.author.__str__()

    author = models.CharField(verbose_name="Автор", max_length=256)
    question = models.TextField(verbose_name="Вопрос")
    answer = models.TextField(verbose_name="Ответ", null=True, blank=True)
