# Generated by Django 3.0 on 2019-12-19 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voluntariapp', '0025_auto_20191219_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='week',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='week',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
