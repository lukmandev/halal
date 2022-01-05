# Generated by Django 3.2.8 on 2021-11-29 10:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0003_category_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, related_name='favorite_companies', to=settings.AUTH_USER_MODEL),
        ),
    ]
