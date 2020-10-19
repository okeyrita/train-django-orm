from django.contrib import admin
from .models import Student, Speciality, Course, Professor, Instructor

admin.site.register(Student)
admin.site.register(Speciality)
admin.site.register(Course)
admin.site.register(Professor)
admin.site.register(Instructor)
