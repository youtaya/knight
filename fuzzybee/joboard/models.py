from django.db import models

class Factory(models.Model):
    fact_name = models.CharField(max_length=200)
    fact_addr = models.CharField(max_length=200)
    hire_num = models.IntegerField(default=0)
