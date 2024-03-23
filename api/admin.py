from django.contrib import admin
from .models import Exercise, Workout, Set, WorkoutExercise

# Register your models here.
admin.site.register(
	Exercise
)
admin.site.register(
	Workout
)
admin.site.register(
	Set
)
admin.site.register(
	WorkoutExercise
)