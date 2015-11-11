from django.db import models

# Create your models here.
class Jobseeker(models.Model):
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	DOB = models.DateTimeField()

class Company(models.Model):
	name = models.CharField(max_length=255)
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
