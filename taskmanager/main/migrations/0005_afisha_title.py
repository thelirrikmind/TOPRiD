# Generated by Django 4.0.4 on 2022-06-16 16:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0004_remove_afisha_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='afisha',
            name='title',
            field=models.CharField(default=2, max_length=50, verbose_name='Название'),
            preserve_default=False,
        ),
    ]
