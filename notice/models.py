from django.db import models
from django.conf import settings
from django.utils import timezone

class Notices(models.Model):  
	eid = models.CharField(max_length=20, blank=True, null=True)  
	title = models.CharField(max_length=100, blank=True, null=True)  
	files=models.FileField(upload_to='notices/',blank=True, null=True)
	created_date=models.DateTimeField( blank=True, null=True)
	description = models.TextField(blank=True, null=True) 
	class Meta:  
		db_table = "notices"  

