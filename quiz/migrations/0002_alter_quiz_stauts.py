# Generated by Django 4.0.2 on 2023-05-26 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='stauts',
            field=models.CharField(choices=[('inactive', 'Inactive'), ('active', 'Active'), ('finished', 'Finished')], default='inactive', max_length=10),
        ),
    ]