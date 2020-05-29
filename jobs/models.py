from django.db import models
from django.urls import reverse

class Job(models.Model):
	 title = models.CharField(max_length=20, default='Programmer')
	 image = models.ImageField(upload_to='images/')
	 summary = models.CharField(max_length=200)
	 uri = models.CharField(max_length=50, default="home")