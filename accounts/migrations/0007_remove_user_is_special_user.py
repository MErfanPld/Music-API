# Generated by Django 4.2.4 on 2023-08-23 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_user_is_special_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_special_user',
        ),
    ]