# Generated by Django 2.0.4 on 2018-05-13 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_date',
            field=models.DateField(),
        ),
    ]
