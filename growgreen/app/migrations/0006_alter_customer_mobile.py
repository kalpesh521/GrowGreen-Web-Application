# Generated by Django 4.2.1 on 2023-06-24 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_customer_mobile_alter_customer_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.BigIntegerField(),
        ),
    ]
