# Generated by Django 3.2.9 on 2021-11-17 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_alter_user_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='basket',
        ),
    ]