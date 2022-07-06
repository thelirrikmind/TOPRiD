from django.db import models


class Task(models.Model):
    title = models.CharField('Заголовок новости', max_length=50)
    task = models.TextField('Содержание новости',default='', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Image(models.Model):
    title = models.CharField('Имя', max_length=50)
    image = models.ImageField('Фото', upload_to='images/users/%Y/%m/%d', blank=True)
    task = models.TextField('Биография', default='', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сотрудника'
        verbose_name_plural = 'Труппа'


class Afisha(models.Model):
    title = models.CharField('Название', max_length=50)
    image = models.ImageField('Фото', upload_to='afisha/users/%Y/%m/%d')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Афишу'
        verbose_name_plural = 'Афиши'


class Album(models.Model):
    title = models.CharField(max_length=127, default='Без названия')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'


class Photo(models.Model):
    image = models.ImageField('Фото', upload_to='Photo/users/%Y/%m/%d')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="photos", null=True)

    def __str__(self):
        return self.album.title

    class Meta:
        verbose_name = 'Фотографию'
        verbose_name_plural = 'Фотографии'
