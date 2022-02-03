
from email.mime import image
from turtle import title
from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.


class Evening(models.Model):
	title = models.CharField(max_length=100)
	file = models.FileField(upload_to='notices/', blank=True, null=True)
	type = models.BooleanField(default=True)


class Team(models.Model):
	#A good rule of thumb is that you use 
	#CharField when you need to limit the maximum length, TextField otherwise.
	title = models.CharField(max_length = 30)
	image= models.ImageField(upload_to='team/',blank=True, null=True)
	#created_date=models.DateTimeField(default=timezone.now)
	#published_date=models.DateTimeField(blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	# core = models.BooleanField(default=False)
	batches = [
		('Final','Final'),
		('Third','Third')
	]
	batch = models.CharField(max_length=30, choices=batches,default='Final')

	def __str__(self):
		return self.title


	def summary(self):
		return self.decription[:100]
# Model for Alumni
class Alumni(models.Model):
	title = models.CharField(max_length=30)
	image = models.ImageField(upload_to='team/',blank=True,null=True)
	description = models.TextField(blank=True,null=True)
	batches = [
		('First','2016-20'),
		('Second','2017-21')
	]
	batch = models.CharField(max_length=30, choices=batches,default='2016-20')
	def __str__(self):
		return self.title


	def summary(self):
		return self.decription[:100]

class News(models.Model):
	title = models.CharField(max_length=100)
	desc = models.CharField(max_length=250)
	date = models.DateField()
	pic = models.ImageField(upload_to='news/', blank=True, null=True)


class Volunteer(models.Model):
	mem_id = models.CharField(max_length=100, blank=True, null=True)
	description = models.CharField(max_length=200)
	date = models.DateField()
	type = models.CharField(max_length=100)


class Member(models.Model):
	name = models.CharField(max_length=100)								#changes
	mob = models.CharField(max_length=100)
	alum = models.BooleanField(default=False)
	batch = models.CharField(max_length=100, default="-1", blank=True, null=True)
	loc = models.CharField(max_length=100)
	mail = models.EmailField(max_length=100)
	about = models.CharField(max_length = 200, blank=True, null=True)
