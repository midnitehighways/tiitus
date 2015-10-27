from django.db import models
#from django_countries.fields import CountryField

# Create your models here.
class Jobseeker(models.Model):
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
#	country = CountryField()
	country = models.CharField(max_length=50, default='Finland')
	city = models.CharField(max_length=50, default='Helsinki')
	DOB = models.DateTimeField()
	photo = models.ImageField(upload_to='photos', null=True)
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
	description_short = models.CharField(max_length=500, blank=True)
	description_full = models.CharField(max_length=2000, blank=True)
	interests = models.CharField(max_length=500, blank=True)
	phone = models.CharField(max_length=30, blank=True)
	email = models.CharField(max_length=50, blank=True)

	def __str__(self):
		return self.lastname

class Company(models.Model):
	name = models.CharField(max_length=100)
	advertisement_short = models.CharField(max_length=500)
	advertisement_full = models.CharField(max_length=2000, blank=True)