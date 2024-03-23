from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Exercise(models.Model):
        name = models.CharField(max_length=100)
        muscle_group = models.CharField(max_length=50)
        created_date = models.DateTimeField(default=timezone.now)

        def __str__(self):
            return self.name
        
class Workout(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      name = models.CharField(max_length=100)

      def __str__(self):
            return self.name

class Set(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    reps = models.IntegerField()
    weight = models.FloatField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.exercise.name)
    
class WorkoutExercise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.ManyToManyField(Set)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.workout.name} - {self.exercise.name}"