# Generated by Django 4.0.2 on 2023-05-26 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_alter_quiz_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quiz',
            old_name='stauts',
            new_name='quiz_stauts',
        ),
    ]
