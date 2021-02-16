from django.db import models
from PIL import Image
class Post(models.Model):
    brand = models.CharField('BRAND', max_length=10)
    title = models.CharField(verbose_name='TITLE', max_length=50)
    price = models.IntegerField(null=True)
    date = models.CharField(max_length=100, null=True)
    date_int = models.IntegerField(null=True)
    image = models.ImageField(blank=True, null=True)

    def __unicode__(self):
        return self.title

    class Meta :
        db_table = 'search_lists'

