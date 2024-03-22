from django.shortcuts import render
from django.http import JsonResponse
from .models import Exercises

# Create your views here.
def exercises(request):
	exercises = Exercises.objects.all()
	return JsonResponse(list(exercises.values()), safe=False)