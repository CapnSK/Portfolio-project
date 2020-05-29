from django.db import models

class Achievment(models.Model):
	title = models.CharField(max_length=50)
	#image = models.ImageField(upload_to='images/')
	summary = models.TextField(max_length=500)