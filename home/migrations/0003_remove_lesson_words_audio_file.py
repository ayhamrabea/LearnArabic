# Generated by Django 4.2.4 on 2023-11-22 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_lesson_words_audio_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson_words',
            name='audio_file',
        ),
    ]
