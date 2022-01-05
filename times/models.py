from django.db import models


class Time(models.Model):

    class Meta:
        verbose_name = "Дата и Время"
        verbose_name_plural = "Даты и Времена"

    def __str__(self):
        return self.date.__str__()

    first_time = models.TimeField(verbose_name="Фаджр")
    second_time = models.TimeField(verbose_name="Восход")
    third_time = models.TimeField(verbose_name="Зухр")
    fourth_time = models.TimeField(verbose_name="Аср")
    fifth_time = models.TimeField(verbose_name="Магриб")
    seventh_time = models.TimeField(verbose_name="Иша")
    sixth_time = models.TimeField(verbose_name="Тахажжуд")
    date = models.DateField(verbose_name="Дата")

