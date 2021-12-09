# Generated by Django 3.2.9 on 2021-11-17 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_alter_user_status'),
        ('products', '0003_auto_20211116_1420'),
        ('details', '0003_basket_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='user'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=1)),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='details.basket', verbose_name='basket')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]