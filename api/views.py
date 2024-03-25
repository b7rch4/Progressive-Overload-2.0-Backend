from django.shortcuts import render
from django.http import JsonResponse
from .models import Exercise, Workout, Set, WorkoutExercise

# Create your views here.
def exercises(request):
	exercises = Exercise.objects.all()
	return JsonResponse(list(exercises.values()), safe=False)

def back_biceps(request):
    data = WorkoutExercise.objects.filter(workout__name="Back and Biceps").prefetch_related('sets')
    serialized_data = []
    for d in data:
        serialized_data.append({
			'workout_id': d.workout.id,
			'exercise+id': d.exercise.id,
			'sets': list(d.sets.values()),
		})
    return JsonResponse(list(serialized_data), safe=False)
