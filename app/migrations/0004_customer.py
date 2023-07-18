# Generated by Django 4.2.1 on 2023-06-14 13:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('locality', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('mobile', models.IntegerField(default=0)),
                ('zipcode', models.IntegerField(default=0)),
                ('state', models.CharField(choices=[('Aandra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Maharashtra', 'Maharashtra'), ('Karnataka', 'Karnataka'), ('Tamil Nadu', 'Tamil Nadu'), ('Kerala', 'Kerala'), ('Gujarat', 'Gujarat'), ('Rajasthan', 'Rajasthan'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Jharkhand', 'Jharkhand'), ('Bihar', 'Bihar'), ('West Bengal', 'West Bengal'), ('Odisha', 'Odisha'), ('Assam', 'Assam'), ('Punjab', 'Punjab'), ('Haryana', 'Haryana'), ('Chhattisgarh', 'Chhattisgarh'), ('Uttarakhand', 'Uttarakhand'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Tripura', 'Tripura'), ('Meghalaya', 'Meghalaya'), ('Manipur', 'Manipur'), ('Nagaland', 'Nagaland'), ('Goa', 'Goa'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Mizoram', 'Mizoram'), ('Sikkim', 'Sikkim'), ('Delhi', 'Delhi'), ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Puducherry', 'Puducherry'), ('Chandigarh', 'Chandigarh'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]