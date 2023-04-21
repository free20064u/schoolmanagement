from django.contrib.auth.models import User, AbstractUser
from django.db import models


# Create your models here.
class Program(models.Model):
    programName = models.CharField(max_length=255,null=True, blank=True, default='')
    fees = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.programName
    

class CustomUser(AbstractUser):
    program = models.ForeignKey(Program,on_delete=models.CASCADE, blank=True, null=True)
    indexNo = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='media', blank=True, default='')
    is_student = models.BooleanField(default=False)
    paid = models.IntegerField(blank=True, null=True, default=0)

    def bal(self):
        balance = self.program.fees - self.paid
        return balance 

    

  


