# Generated by Django 3.2.8 on 2021-10-09 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.TextField(blank=True, null=True, verbose_name='Ответ'),
        ),
    ]