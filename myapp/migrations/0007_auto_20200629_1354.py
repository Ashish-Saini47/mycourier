# Generated by Django 3.0.6 on 2020-06-29 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_courier_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courier_details',
            name='date',
            field=models.DateField(),
        ),
    ]