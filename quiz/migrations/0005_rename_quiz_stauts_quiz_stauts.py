# Generated by Django 4.0.2 on 2023-05-26 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_rename_stauts_quiz_quiz_stauts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='quiz_stauts',
            new_name='stauts',
        ),
    ]
