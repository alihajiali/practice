# Generated by Django 3.2.9 on 2021-11-24 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20211124_1944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='picture',
            new_name='post',
        ),
    ]
