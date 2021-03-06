# Generated by Django 3.2.9 on 2021-11-16 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('fullname', models.CharField(max_length=254, verbose_name='full name')),
                ('username', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='user name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('password', models.CharField(max_length=50, verbose_name='password')),
                ('status', models.CharField(choices=[('c', 'customer'), ('s', 'seller')], default='s', max_length=1, verbose_name='status')),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='details.basket', verbose_name='basket')),
            ],
        ),
    ]
