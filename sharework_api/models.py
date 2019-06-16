from django.db import models

# Create your models here.


class Urls(models.Model):
    id = models.AutoField(db_column='url_id', primary_key=True)
    short_url = models.SlugField(db_column='short_url',)
    title = models.CharField(
        db_column='title', max_length=255, blank=False, default='')
    created = models.DateTimeField(db_column='created', auto_now_add=True)

    class Meta:
        ordering = ('-created',)
