from django.contrib.auth.models import User
from django.db import models


class MyManager(models.Manager):
    def custom_filter(self, **kwargs):
        kwargs['published'] = True
        return super().get_queryset().filter(**kwargs)

    def custom_order_by(self, *args):
        args = ('published', ) + args
        return super().get_queryset().order_by(*args)


class Post(models.Model):
    title = models.CharField("Называние", max_length=50)
    text = models.TextField("Описание")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post', verbose_name='Автор')
    members = models.ManyToManyField(User, related_name='members', blank=True, verbose_name='Участники')
    published = models.BooleanField()

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title

    objects = models.Manager()
    custom_manager = MyManager()
