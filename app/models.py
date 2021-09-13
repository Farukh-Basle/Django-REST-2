from django.db import models

# Create your models here.
class Emp(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=100)
    esal = models.FloatField()


    def __str__(self):
        return self.ename   #to showing object is created