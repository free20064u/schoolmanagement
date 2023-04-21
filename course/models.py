from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Program(models.Model):
    programName = models.CharField(max_length=255, blank=True, default='')
    fees = models.IntegerField(unique=True)

    def __str__(self):
        return self.programName


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.RESTRICT)
    indexNo = models.IntegerField()
    image = models.ImageField(upload_to='media', blank=True, default='')
    paid = models.IntegerField()

    def __str__(self):
        return str(self.user)
    
    def bal(self):
        balance = self.program.fees - self.paid
        return balance 

  


