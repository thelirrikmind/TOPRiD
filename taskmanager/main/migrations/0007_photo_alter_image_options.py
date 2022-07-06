# Generated by Django 4.0.4 on 2022-06-16 16:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0006_alter_image_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('image', models.ImageField(upload_to='Photo/users/%Y/%m/%d', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
            },
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Труппа', 'verbose_name_plural': 'Труппа'},
        ),
    ]