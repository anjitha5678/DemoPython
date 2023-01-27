from django.db import models

# Create your models here.
class School(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pictures')
    desc=models.TextField()

    def  __str__(self):
        return self.name
class Store(models.Model):

    img=models.ImageField(upload_to='pictures')
    desc=models.TextField()


