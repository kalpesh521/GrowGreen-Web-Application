# Generated by Django 4.2.1 on 2023-06-01 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounter_price', models.FloatField()),
                ('category', models.CharField(choices=[('CR', 'Curd'), ('CH', 'Cheese'), ('BU', 'Butter'), ('MI', 'Milk'), ('OT', 'Other')], max_length=2)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='products')),
            ],
        ),
    ]
