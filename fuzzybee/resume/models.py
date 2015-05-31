from django.db import models
from joboard.models import Factory

class Resume(models.Model):
    apply_factory = models.ForeignKey(Factory, related_name='factory')
    identity_image = models.ImageField(upload_to='identity')
    name = models.CharField(max_length=24, blank=True)
    gender = models.CharField(max_length=4)
    birthday = models.CharField(max_length=24)
    experience = models.CharField(max_length=24)
    education = models.CharField(max_length=24)
    phone = models.CharField(max_length=24)
    apply_job = models.CharField(max_length=24)
    expect_salary = models.CharField(max_length=24)
    self_description = models.CharField(max_length=100)
