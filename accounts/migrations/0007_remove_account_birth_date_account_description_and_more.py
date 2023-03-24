# Generated by Django 4.1.7 on 2023-03-24 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_account_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='birth_date',
        ),
        migrations.AddField(
            model_name='account',
            name='description',
            field=models.CharField(max_length=500, null=True, verbose_name='Информация о пользователе'),
        ),
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=models.ImageField(default=None, null=True, upload_to='user_pic', verbose_name='Аватар'),
        ),
    ]