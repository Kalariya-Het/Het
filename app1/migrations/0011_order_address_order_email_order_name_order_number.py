# Generated by Django 4.2.4 on 2023-08-16 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_cart_productprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='order',
            name='number',
            field=models.CharField(default='', max_length=200),
        ),
    ]
