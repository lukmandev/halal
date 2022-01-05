from django.db import models


class Banner(models.Model):

    class Meta:
        verbose_name = "Реклама"
        verbose_name_plural = "Рекламы"

    def __str__(self):
        return self.banner.__str__()

    banner = models.ImageField(verbose_name="Фото рекламы", upload_to='banners/')
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
