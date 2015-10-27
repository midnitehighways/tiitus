from django.shortcuts import render
import random
from .models import Position

# Create your views here.
def home(request):
  position = Position.objects.order_by('?').last()
  return render(request, 'home/position.html', {'position': position})
