from django.shortcuts import get_object_or_404, render
from .models import Jobseeker, Company

def index(request):
	person_list = Jobseeker.objects.order_by('lastname')
	return render(request, 'app/index.html', {'person_list': person_list})
