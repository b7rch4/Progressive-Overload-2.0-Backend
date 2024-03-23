from django.shortcuts import render
from django.http import JsonResponse
from .models import Exercise

# Create your views here.
def exercises(request):
	exercises = Exercise.objects.all()
	return JsonResponse(list(exercises.values()), safe=False)