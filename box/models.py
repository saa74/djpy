from django.db import models


class Tags(models.Model):
    name = models.CharField(max_length=50, verbose_name='Тег')

    class Meta:
        verbose_name='Тег'
        verbose_name_plural='Теги'
    
    def __str__(self):
        return self.name


class Articles(models.Model):
    name = models.CharField(max_length=50, verbose_name='Заголовок')
    menu_name = models.CharField(blank = True, max_length=30, verbose_name='Имя в Меню')
    menu_visible = models.BooleanField(default=0, verbose_name='Виден в Меню')
    description = models.TextField(verbose_name='Описание')
    keywords =  models.CharField(blank = True, max_length=50, verbose_name='Ключевые слова')
    tag = models.ManyToManyField(Tags, verbose_name='Теги')
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name='Статья'
        verbose_name_plural='Статьи'
    
    def __str__(self):
        return self.name
