# Generated by Django 3.0 on 2019-12-19 10:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('voluntariapp', '0024_auto_20191217_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='week',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='week',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]