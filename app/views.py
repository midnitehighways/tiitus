import random
from django.shortcuts import get_object_or_404, render
from .models import Position, Jobseeker, Company
from social_auth.models import UserSocialAuth

# Create your views here.
def home(request):
  position = Position.objects.order_by('?').last()
  return render(request, 'home/position.html', {'position': position})

def index(request):
	person_list = Jobseeker.objects.order_by('lastname')
        if request.user.is_authenticated():
		collection = UserSocialAuth.objects.filter(user_id=request.user.id)
		if collection:
			user_social_auth = collection.get().extra_data
		else: 
			user_social_auth = {}

        else:
		user_social_auth = {}
	return render(request, 'app/index.html', {'person_list': person_list, 'user_meta': user_social_auth})
