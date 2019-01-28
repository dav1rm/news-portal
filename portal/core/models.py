from django.db import models

class NoticeManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(name_icontains=query)


class Notice(models.Model):
    title = models.CharField('Título', max_length=300)
    objects = NoticeManager()