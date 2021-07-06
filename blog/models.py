from django.db import models


class Article(models.Model):
    title = models.CharField('Название', max_length=100)
    content = models.TextField('Содержимое статьи')
    pub_date = models.DateTimeField('Дата публикации', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    name = models.CharField('Имя', max_length=100)
    content = models.CharField('Текст комментария', max_length=200)
    pub_date = models.DateTimeField('Дата публикации', auto_now=True)
    art = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
