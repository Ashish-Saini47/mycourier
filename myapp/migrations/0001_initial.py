# Generated by Django 3.0.6 on 2020-06-27 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=120)),
                ('phone_number', models.IntegerField()),
                ('query', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
