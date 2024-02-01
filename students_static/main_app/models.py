from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
DEFAULT = 'photos/img.JPG.jpg'
class Gander(models.Model):
    male_famale = models.CharField(max_length=50)
    
    def __str__ (self):
        return str(self.male_famale)

class Lavel(models.Model):
    students_lavel = models.CharField(max_length=50)
    
    
    def __str__ (self):
        return str(self.students_lavel)

class Student(models.Model):
    student_name = models.CharField(max_length=50)
    slug_name = models.SlugField(max_length=50)
    age = models.PositiveIntegerField(default=0)
    data_time = models.DateTimeField(auto_now_add=True)
    commentarya = models.TextField(blank=True)
    gander = models.ForeignKey(Gander , 
                               on_delete=models.CASCADE,  null=True)
    payment = models.BooleanField(default=False)
    lavel = models.ForeignKey(Lavel , 
                              on_delete=models.CASCADE , null=True)
    like = models.PositiveIntegerField(default=0 , blank=True)
    admin = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               null=True)
    img = models.ImageField(upload_to='photos/' , blank=True , default=DEFAULT)
    descrition = models.TextField()
    rating = models.PositiveIntegerField(default=0)


    def __str__ (self):
        return str(self.student_name)


class Comment(models.Model):
    user_name = models.CharField(max_length=50 , null=True , blank=True)
    coments = models.TextField()
    post = models.ForeignKey(Student,
                             on_delete=models.CASCADE,null=True,
                             related_name='comentary')

    
    def __str__ (self):
        return str(self.user_name)