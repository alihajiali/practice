# Generated by Django 3.2.9 on 2021-11-16 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('s', 'seller'), ('c', 'customer')], default='s', max_length=1, verbose_name='status'),
        ),
    ]