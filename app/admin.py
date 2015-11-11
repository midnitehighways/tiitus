from django.contrib import admin
from app.models import Jobseeker, Company, Position
# Register your models here.
class JobseekerAdmin(admin.ModelAdmin):
  pass

admin.site.register(Jobseeker, JobseekerAdmin)

class CompanyAdmin(admin.ModelAdmin):
  pass

admin.site.register(Company, CompanyAdmin)

class PositionAdmin(admin.ModelAdmin):
  pass

admin.site.register(Position, PositionAdmin)

