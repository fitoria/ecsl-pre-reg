from django.db import models
from django.contrib.auth.models import User 

class Feed(models.Model):
    title = models.CharField('Titulo', max_length = 500)
    slug = models.SlugField('url amigable', unique = True)
    feed_url = models.URLField('url del feed', unique = True, max_length = 500)
    public_url = models.URLField('url publica', max_length = 500)
    is_active = models.BooleanField('Activo?', default = True)

    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return '/planeta/autor/%s' % self.slug

class FeedItem(models.Model):
    feed = models.ForeignKey( Feed)
    title = models.CharField('Titulo', max_length = 500)
    link = models.URLField(max_length = 500)
    summary = models.TextField('Contenido', blank = True)
    date_modified = models.DateTimeField('fecha')
    guid = models.CharField(max_length = 500, unique = True, db_index = True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ("-date_modified",)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/planeta/articulo/%d' % self.id
