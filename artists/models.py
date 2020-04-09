from django.db import models

class artist(models.Model):
	name=models.CharField(max_length=100,default="None")
	DOB=models.DateField()
	bio=models.TextField()

	def __str__(self):
		return self.name