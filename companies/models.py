from django.db import models

from users.models import User


class Category(models.Model):

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name.__str__()

    logo = models.ImageField(verbose_name="Логотип категории", upload_to='images', null=True)
    title_ky = models.CharField(verbose_name="Название категории", max_length=100)
    title_ru = models.CharField(verbose_name="Название категории", max_length=100)


class Company(models.Model):

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    def __str__(self):
        return self.name.__str__()

    logo = models.ImageField(verbose_name="Логотип компании", upload_to='images', null=True, blank=True)
    name = models.CharField(verbose_name="Название компании", max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    users = models.ManyToManyField(User, related_name='favorite_companies', null=True, blank=True)


class Product(models.Model):

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.title.__str__()

    photo = models.ImageField(verbose_name="Фото продукта", upload_to='images', null=True, blank=True)
    title_ky = models.CharField(verbose_name="Название продукта", max_length=100)
    title_ru = models.CharField(verbose_name="Название продукта", max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
