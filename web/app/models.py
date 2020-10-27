from django.db import models

# Create your models here.
class Patients(models.Model):
    
    GENDER = (
        (1, 1), 
        (2, 2),
    )
    CHOLESTEROL = (
        (1, 1), 
        (2, 2), 
        (3, 3),
    )
    GLUCOSE = (
        (1, 1), 
        (2, 2), 
        (3, 3),
    )
    SMOKER = (
        (0, "No"), 
        (1, "YES"),
    )
    ALCOHOL = (
        (0, "NO"), 
        (1, "YES"),
    )
    ACTIVE = (
        (0, "Sedentary"), 
        (1, "Active Person"),
    )

    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.IntegerField(null=True, blank=True, choices=GENDER)
    height = models.IntegerField(null=True, blank=True)
    weight = models.DecimalField(decimal_places=2, max_digits=4, null=True, blank=True)
    hight_pressure = models.IntegerField(null=True, blank=True)
    low_pressure = models.IntegerField(null=True, blank=True)
    cholesterol = models.IntegerField(null=True, blank=True, choices=CHOLESTEROL)
    glucose = models.IntegerField(null=True, blank=True, choices=GLUCOSE)
    smoker = models.IntegerField(null=True, blank=True, choices=SMOKER)
    alcohol = models.IntegerField(null=True, blank=True, choices=ALCOHOL)
    active = models.IntegerField(null=True, blank=True, choices=ACTIVE)
    cardio = models.IntegerField(null=True, blank=True, default=0)
    
    
    def __str__(self):
        return self.name