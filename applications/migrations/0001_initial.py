# Generated by Django 3.2.8 on 2021-11-29 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=500, verbose_name='Имя компании')),
                ('inn', models.CharField(max_length=25, verbose_name='ИНН')),
                ('product_type', models.CharField(max_length=500, verbose_name='Тип продукта')),
                ('name', models.CharField(max_length=500, verbose_name='ФИО')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]