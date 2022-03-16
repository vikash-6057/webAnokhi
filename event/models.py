from django.db import models
from django.conf import settings
from django.utils import timezone

class Events(models.Model):
	#A good rule of thumb is that you use 
	#CharField when you need to limit the maximum length, TextField otherwise.
	title = models.CharField(max_length = 30)
	#files= models.FileField(upload_to='noticefiles/',blank=True, null=True)
	published_date=models.DateTimeField(blank=True, null=True)
	image= models.ImageField(upload_to='events/',blank=True, null=True)
	decription = models.TextField()


	def __str__(self):
		return self.title


	def summary(self):
		return self.decription[:100]

	def pub_date_pretty(self):
		return self.published_date.strftime('%b %e %Y')

class Gallery(models.Model):
	#A good rule of thumb is that you use 
	#CharField when you need to limit the maximum length, TextField otherwise.
	title = models.CharField(max_length = 30 ,blank=True, null=True)
	image= models.ImageField(upload_to='events/',blank=True, null=True)
	description=models.CharField(max_length=80,blank=True,null=True)
	category = models.ForeignKey(Events,on_delete=models.CASCADE)


class Program(models.Model):
	title = models.CharField(max_length = 100 ,blank=True, null=True)
	image= models.ImageField(upload_to='events/',blank=True, null=True)
	description=models.CharField(max_length=500,blank=True,null=True)
	date = models.DateTimeField(blank=True, null=True)

