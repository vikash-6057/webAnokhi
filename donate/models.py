from django.db import models

# Create your models here.


class Donors(models.Model):
    name = models.CharField(max_length=200)
    message = models.CharField(max_length=100)
    amount = models.CharField(max_length=200)
    date = models.DateField()
    mob = models.CharField(max_length=100, blank=True, null=True)
    tran_id = models.CharField(max_length=100, blank=True, null=True)
    mode = models.CharField(max_length=100, blank=True, null=True)
    verified = models.BooleanField(default=False)
    mem_id = models.CharField(max_length=100, blank=True, null=True)

