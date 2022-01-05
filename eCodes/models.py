from django.db import models


E_CODE_CHOICES = (
    ('good', 'Халал'),
    ('doubt', 'Сомнительно'),
    ('harm', 'Харам')
)


class ECode(models.Model):

    class Meta:
        verbose_name = 'Код'
        verbose_name_plural = 'Е коды'

    def __str__(self):
        return self.code.__str__()

    code = models.CharField(verbose_name='Код', max_length=15)
    title_ky = models.TextField(verbose_name='Описание')
    title_ru = models.TextField(verbose_name='Описание')
    type = models.CharField(verbose_name='Тип', choices=E_CODE_CHOICES, max_length=100)
    damage_description_ru = models.TextField(verbose_name='Вредность')
    damage_description_ky = models.TextField(verbose_name='Вредность')
    useful_description_ru = models.TextField(verbose_name='Полезность')
    useful_description_ky = models.TextField(verbose_name='Полезность')
    use_description_ky = models.TextField(verbose_name='Использование')
    use_description_ru = models.TextField(verbose_name='Использование')

