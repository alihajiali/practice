# Generated by Django 3.2.9 on 2021-11-25 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20211125_1305'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='post',
            unique_together={('title', 'slug')},
        ),
    ]
