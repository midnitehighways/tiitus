import random
from django.shortcuts import get_object_or_404, render
from .models import Position, Jobseeker, Company

# Create your views here.
def home(request):
  position = Position.objects.order_by('?').last()
  return render(request, 'home/position.html', {'position': position})

def index(request):
	person_list = Jobseeker.objects.order_by('lastname')
	return render(request, 'app/index.html', {'person_list': person_list})
