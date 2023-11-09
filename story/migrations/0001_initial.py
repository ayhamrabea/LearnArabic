# Generated by Django 4.2.4 on 2023-11-08 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, null=True, upload_to='story/images')),
                ('audio', models.FileField(blank=True, null=True, upload_to='story/audios')),
            ],
            options={
                'verbose_name': 'Story',
                'verbose_name_plural': 'Storys',
            },
        ),
        migrations.CreateModel(
            name='Parargraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.TextField()),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='story.story')),
            ],
            options={
                'verbose_name': 'Parargraph',
                'verbose_name_plural': 'Parargraphs',
            },
        ),
    ]
