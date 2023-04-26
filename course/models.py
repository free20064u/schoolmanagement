from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.utils.text import slugify
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill

# Create your models here.
class Program(models.Model):
    programName = models.CharField(max_length=255)
    fees = models.IntegerField()

    def __str__(self):
        return self.programName
    

class CustomUser(AbstractUser):
    program = models.ForeignKey(Program,on_delete=models.CASCADE, blank=True, null=True)
    indexNo = models.IntegerField(default=000000, null=True)
    image = models.ImageField(upload_to='media', blank=True, default='', null=True)
    is_student = models.BooleanField(default=True, null=True)
    paid = models.IntegerField(blank=True, default=0, null=True)
    slug = models.SlugField(blank=True, default='')

    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(200, 200)],
                                     format='JPEG',
                                     options={'quality': 60})
    def bal(self):
        balance = self.program.fees - self.paid
        return balance 

    def save(self, *args , **kwargs):
        self.slug = slugify(str(self.indexNo) + self.first_name)
        super(CustomUser, self).save()
    


