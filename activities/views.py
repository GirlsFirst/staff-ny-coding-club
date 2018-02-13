from django.shortcuts import render
from django.utils import timezone
from .models import Activity

# Create your views here.
def activity_list(request):
  activities = Activity.objects.order_by('published_date')
  return render(request, 'activities/activity_list.html', {})