from django.db import models

# Create your models here.


class Application(models.Model):

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    company_name = models.CharField(max_length=500, verbose_name="Имя компании")
    address = models.CharField(max_length=25, verbose_name="Адрес")
    product_type = models.CharField(max_length=500, verbose_name="Тип продукта")

    name = models.CharField(max_length=500, verbose_name="ФИО")
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")

    def __str__(self):
        return self.company_name