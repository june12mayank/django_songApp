from django.db import models

class song(models.Model):
	img=models.ImageField(upload_to='images/')
	name=models.CharField(max_length=100)
	DOR=models.DateField()

	def __str__(self):
		return self.name