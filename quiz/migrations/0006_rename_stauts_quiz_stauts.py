# Generated by Django 4.0.2 on 2023-05-26 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_rename_quiz_stauts_quiz_stauts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='stauts',
            new_name='Stauts',
        ),
    ]