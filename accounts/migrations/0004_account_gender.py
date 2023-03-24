# Generated by Django 4.1.7 on 2023-03-24 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_account_avatar_alter_account_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Мужской'), ('F', 'Женский'), ('N', 'Не указано')], default='N', max_length=1, verbose_name='Пол'),
        ),
    ]