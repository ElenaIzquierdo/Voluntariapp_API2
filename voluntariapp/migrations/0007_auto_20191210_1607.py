# Generated by Django 3.0 on 2019-12-10 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voluntariapp', '0006_auto_20191210_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forumtheme',
            name='tasks',
        ),
        migrations.AddField(
            model_name='forumtheme',
            name='group',
            field=models.TextField(default='Petits'),
            preserve_default=False,
        ),
    ]