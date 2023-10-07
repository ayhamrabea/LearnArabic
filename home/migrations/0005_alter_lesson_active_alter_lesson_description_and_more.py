# Generated by Django 4.2.4 on 2023-09-27 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_lesson_words_lesson_word_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='active',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='leavel',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='numper_of_lesson',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lesson_words',
            name='lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.lesson'),
        ),
        migrations.AlterField(
            model_name='lesson_words',
            name='lesson_word_id',
            field=models.IntegerField(blank=True, default=99, null=True),
        ),
        migrations.AlterField(
            model_name='lesson_words',
            name='word_AR',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lesson_words',
            name='word_RU',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='said_question',
            name='lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.lesson'),
        ),
        migrations.AlterField(
            model_name='said_question',
            name='question',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='said_question',
            name='said_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]