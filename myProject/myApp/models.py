from django.db import models

class studentmodel(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    date_of_birth=models.DateField()
    father_name=models.CharField(max_length=100)
    mother_name=models.CharField(max_length=100)
    address=models.TextField()
    img=models.ImageField(upload_to='student_photos/')
class teachermodel(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    date_of_birth=models.DateField()
    department=models.CharField()
    address=models.TextField()
