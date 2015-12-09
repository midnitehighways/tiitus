import random
from django.shortcuts import get_object_or_404, render
from .models import Position, Jobseeker, Company, Profile
from social_auth.models import UserSocialAuth
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers
import json
from django.core.mail import send_mail

@csrf_exempt
@login_required
def apply_position(request):
  if request.method == "GET":
    return HttpResponse("GET now allowed")

  position = Position.objects.get(pk=request.GET['id'])
  
  collection = UserSocialAuth.objects.filter(user_id=request.user.id)
  if collection:
    user_meta = collection.get().extra_data
  else: 
    user_meta = {}

  if position.company.contact_email:
    email_from = 'tiitus@inbox.lv'
    message = "%s applied for position %s" % (user_meta['first_name'], position.title)
    send_mail('New job application from Tiitus', message, email_from, [position.company.contact_email], fail_silently=False)

  return HttpResponse("")

def positions(request):
  positions = [pos.json() for pos in Position.objects.all()]
  return HttpResponse(json.dumps(positions), content_type='application/json')

# Create your views here.
def home(request):
  position = Position.objects.order_by('?').last()
  return render(request, 'home/position.html', {'position': position})

@csrf_exempt
@login_required
def profile(request):
  if request.method == 'POST':
    collection = Profile.objects.filter(user_id=request.user.id)
    if collection:
      profile = collection.get()
    else: 
      profile = Profile(user=request.user)

    profile.about = request.POST['about']
    profile.skills = request.POST['skills']
    profile.interest = request.POST['interest']
    profile.speciality = request.POST['speciality']
    profile.save()

    return HttpResponse("")
  else:
    return HttpResponse('GET not allowed')

def index(request):
  if request.user.is_authenticated():
    if request.user.is_superuser:
      return HttpResponse('Jobseeker page not allowed for admin')

    collection = UserSocialAuth.objects.filter(user_id=request.user.id)
    if collection:
      user_meta = collection.get().extra_data
    else: 
      user_meta = {}

    return render(request, 'app/intro.html', {'user_meta': json.dumps(user_meta)})
  else:
		return render(request, 'app/index.html')
