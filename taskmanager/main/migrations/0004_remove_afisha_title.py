# Generated by Django 4.0.4 on 2022-06-16 15:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0003_afisha_alter_image_options_alter_task_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='afisha',
            name='title',
        ),
    ]
