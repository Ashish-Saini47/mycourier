# Generated by Django 3.0.6 on 2020-06-29 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20200629_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courier_details',
            name='p_n_time',
            field=models.CharField(max_length=2),
        ),
    ]
