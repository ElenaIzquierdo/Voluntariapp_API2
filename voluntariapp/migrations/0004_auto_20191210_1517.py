# Generated by Django 3.0 on 2019-12-10 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voluntariapp', '0003_centreinteres_comment_eventattendee_forumtheme'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='event',
            name='type',
        ),
        migrations.AddField(
            model_name='event',
            name='group',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
    ]