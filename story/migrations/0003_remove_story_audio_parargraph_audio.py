# Generated by Django 4.2.4 on 2023-12-02 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0002_story_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='audio',
        ),
        migrations.AddField(
            model_name='parargraph',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='story/audios'),
        ),
    ]
