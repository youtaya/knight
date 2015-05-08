from django.db import models
from joboard.fields import PlaceMultiField
from django.utils.encoding import smart_unicode

class PlaceMultiModelField(models.Field):

    def formfield(self, **kwargs):
        defaults = {'form_class': PlaceMultiField}
        defaults.update(kwargs)
        return super(PlaceMultiModelField, self).formfield(**defaults)

    def get_internal_type(self):
        return 'TextField'

class Factory(models.Model):
    fact_name = models.CharField(max_length=200)
    fact_addr = PlaceMultiModelField()
    fact_lat = models.FloatField()
    fact_lng = models.FloatField()
    hire_num = models.IntegerField(default=0)


    def __unicode__(self):
        return smart_unicode(self.fact_name)

    class Meta:
        ordering = ['fact_name','hire_num']
