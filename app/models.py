from django.db import models
#from django_countries.fields import CountryField

# Create your models here.
class Jobseeker(models.Model):
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
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
	name = models.CharField(max_length=255)
	advertisement_short = models.CharField(max_length=500)
	advertisement_full = models.CharField(max_length=2000, blank=True)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = "companies"

class Position(models.Model):
	title = models.CharField(max_length=255)
	company = models.ForeignKey(Company)
        description = models.TextField()
        requirements = models.TextField()
        created_at = models.DateTimeField(auto_now=True)
        def __str__(self):
		return '%s / %s' % (self.title, self.company.name) 
