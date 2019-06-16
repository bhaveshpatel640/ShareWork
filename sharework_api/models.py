from django.db import models

# Create your models here.


class Urls(models.Model):
    id = models.AutoField(db_column='url_id', primary_key=True)
    short_url = models.SlugField(db_column='short_url', blank=False)
    title = models.CharField(
        db_column='title', max_length=255, blank=False, default='')
    long_url = models.URLField(
        db_column='long_url', max_length=5000, blank=False)
    created = models.DateTimeField(db_column='created', auto_now_add=True)
    modified = models.DateTimeField(db_column='modified', auto_now=True)

    class Meta:
        ordering = ('-created',)
