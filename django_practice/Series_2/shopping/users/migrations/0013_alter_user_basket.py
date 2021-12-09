# Generated by Django 3.2.9 on 2021-11-16 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0002_auto_20211116_1430'),
        ('users', '0012_alter_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='basket',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='details.basket', verbose_name='basket'),
        ),
    ]
