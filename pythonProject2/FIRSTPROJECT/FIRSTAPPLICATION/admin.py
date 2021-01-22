from django.contrib import admin
from .models import Student
from .models import Employee
from .models import Teachers


# Register your models here.
admin.site.register(Student)

admin.site.register(Employee)

admin.site.register(Teachers)
