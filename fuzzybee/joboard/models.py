from django.db import models

class Factory(models.Model):
    fact_name = models.CharField(max_length=200)
    fact_addr = models.CharField(max_length=200)
    fact_lat = models.FloatField()
    fact_lng = models.FloatField()
    hire_num = models.IntegerField(default=0)


    def __str__(self):
        return self.fact_name

    class Meta:
        ordering = ['fact_name','hire_num']
