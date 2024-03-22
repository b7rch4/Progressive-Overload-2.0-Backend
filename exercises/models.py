from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

# Create your models here.
class Exercises(models.Model):
        exercise_name = models.CharField(max_length=250)
        muscle_group = models.CharField(max_length=250)
        equipment = models.CharField(max_length=250)
        created_date = models.DateTimeField(default=timezone.now)

        def __str__(self):
            return self.exercise_name