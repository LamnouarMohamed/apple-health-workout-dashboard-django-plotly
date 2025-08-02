from datetime import datetime
from django.db import models

# Create your models here.
class Workout(models.Model):
    workoutActivityType = models.CharField(max_length=70)                       # HKWorkoutActivityTypeRunning
    duration = models.FloatField()                                              # 19.82441914478938 
    durationUnit = models.CharField(max_length=10)                              # "min" 
    sourceName = models.CharField(max_length=50)                                # "Apple Watch" 
    # sourceVersion = models.CharField(max_length=100)                          # "11" 
    device = models.CharField(max_length=100)                                   # "Apple Inc." 
    creationDate = models.DateTimeField()                                       # date  2023-04-30 23:32:12 +0100
    yearCreation = models.IntegerField(null=True, blank=True)
    monthCreation = models.IntegerField(null=True, blank=True)
    dayCreation = models.IntegerField(null=True, blank=True)
    # startDate = models.CharField(max_length=100)                              # date 2023-04-30 23:32:12 +0100
    # endDate = models.CharField(max_length=100)                                # date 2023-04-30 23:32:12 +0100

    def save(self, *args, **kwargs):
        if self.workoutActivityType:
            self.workoutActivityType = self.workoutActivityType.replace("HKWorkoutActivityType", "")  # "HKWorkoutActivityTypeRunning" → "Running"
        if self.creationDate:
            self.yearCreation = self.creationDate.year
            self.monthCreation = self.creationDate.month
            self.dayCreation = self.creationDate.day
        super().save(*args, **kwargs)

class MetadataEntry(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)  

    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, null=True, blank=True)


class WorkoutEvent(models.Model):
    type = models.CharField(max_length=100) 
    date = models.CharField(max_length=100)   # date
    duration = models.CharField(max_length=100, null=True, blank=True) 
    durationUnit = models.CharField(max_length=100, null=True, blank=True)

    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, null=True, blank=True)


class WorkoutStatistics(models.Model):
    type = models.CharField(max_length=100) 
    startDate = models.CharField(max_length=100) 
    endDate = models.CharField(max_length=100) 
    unit = models.CharField(max_length=100) 

    sum = models.CharField(max_length=100, null=True, blank=True)        # models.FloatField(null=True, blank=True)
    average = models.CharField(max_length=100, null=True, blank=True)    # models.FloatField(null=True, blank=True)
    minimum = models.CharField(max_length=100, null=True, blank=True)    # models.FloatField(null=True, blank=True)
    maximum = models.CharField(max_length=100, null=True, blank=True)    # models.FloatField(null=True, blank=True)

    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, null=True, blank=True)


class FileReference(models.Model):
    path = models.CharField(max_length=100, null=True, blank=True)


class WorkoutRoute(models.Model):
    sourceName = models.CharField(max_length=100)
    sourceVersion = models.CharField(max_length=100)
    creationDate = models.CharField(max_length=100)
    startDate = models.CharField(max_length=100)
    endDate = models.CharField(max_length=100)

    workout = models.OneToOneField(Workout, on_delete=models.CASCADE, null=True, blank=True)
    # meta_data_entry_route = models.ForeignKey(MetadataEntry, on_delete=models.CASCADE, null=True, blank=True)
    file_reference = models.OneToOneField(FileReference, on_delete=models.CASCADE, null=True, blank=True)


