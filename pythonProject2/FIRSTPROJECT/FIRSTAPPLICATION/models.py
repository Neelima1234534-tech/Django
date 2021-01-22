from django.db import models

# Create your models here
class Student(models.Model):
        Name = models.CharField(max_length=15)
        Email = models.EmailField(max_length=20)
        Contact = models.DecimalField(decimal_places=2, max_digits=10)
        Address = models.TextField(blank=True, null=True)

class Employee(models.Model):
        Name = models.CharField(max_length=15)
        Email = models.EmailField(max_length=20)
        Contact = models.DecimalField(decimal_places=2, max_digits=10)
        Address = models.TextField(blank=True, null=True)

class Teachers(models.Model):
        Name = models.CharField(max_length=15)
        Email = models.EmailField(max_length=20)
        Contact = models.DecimalField(decimal_places=2, max_digits=10)
        Address = models.TextField(blank=True, null=True)



