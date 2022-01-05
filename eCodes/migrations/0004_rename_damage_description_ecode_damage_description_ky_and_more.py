# Generated by Django 4.0.1 on 2022-01-05 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eCodes', '0003_alter_ecode_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ecode',
            old_name='damage_description',
            new_name='damage_description_ky',
        ),
        migrations.RenameField(
            model_name='ecode',
            old_name='title',
            new_name='title_ky',
        ),
        migrations.RenameField(
            model_name='ecode',
            old_name='use_description',
            new_name='use_description_ky',
        ),
        migrations.RenameField(
            model_name='ecode',
            old_name='useful_description',
            new_name='useful_description_ky',
        ),
        migrations.AddField(
            model_name='ecode',
            name='damage_description_ru',
            field=models.TextField(default='', verbose_name='Вредность'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ecode',
            name='title_ru',
            field=models.TextField(default='', verbose_name='Описание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ecode',
            name='use_description_ru',
            field=models.TextField(default='', verbose_name='Использование'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ecode',
            name='useful_description_ru',
            field=models.TextField(default='', verbose_name='Полезность'),
            preserve_default=False,
        ),
    ]
