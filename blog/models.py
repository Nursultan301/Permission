from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField("Называние", max_length=50)
    text = models.TextField("Описание")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post', verbose_name='Автор')
    members = models.ManyToManyField(User, related_name='members', blank=True, verbose_name='Участники')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title
