from django.db import models
from django.urls import reverse


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='department', blank=True)

    def get_url(self):
        return reverse('deapp:courses_by_department', args=[self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'department'
        verbose_name_plural = 'departments'

    def __str__(self):
        return '{}'.format(self.name)

class Course(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)

    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product', blank=True)

    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('deapp:courDeptdetail',args=[self.department.slug,self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'course'
        verbose_name_plural = 'courses'


    def  __str__(self):
        return  '{}' .format(self.name)


