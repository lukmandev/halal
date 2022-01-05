# Generated by Django 4.0.1 on 2022-01-05 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_alter_company_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='title_ky',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='title_ky',
        ),
        migrations.AddField(
            model_name='category',
            name='title_ru',
            field=models.CharField(default='', max_length=100, verbose_name='Название категории'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='title_ru',
            field=models.CharField(default='', max_length=100, verbose_name='Название продукта'),
            preserve_default=False,
        ),
    ]