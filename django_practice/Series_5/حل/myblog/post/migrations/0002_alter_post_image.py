# Generated by Django 3.2.9 on 2021-11-21 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d'),
        ),
    ]
