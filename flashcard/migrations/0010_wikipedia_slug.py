# Generated by Django 5.1.7 on 2025-04-05 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0009_alter_prompt_code_alter_prompt_mcq'),
    ]

    operations = [
        migrations.AddField(
            model_name='wikipedia',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
