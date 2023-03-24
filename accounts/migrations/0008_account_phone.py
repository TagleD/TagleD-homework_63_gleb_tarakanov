# Generated by Django 4.1.7 on 2023-03-24 06:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_account_birth_date_account_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Номер телефона должен быть в формате: '+79991234567'", regex='^\\+7\\d{10}$')], verbose_name='Номер телефона'),
        ),
    ]
