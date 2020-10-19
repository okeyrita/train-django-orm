from django.db import models
from django.urls import reverse


class Student(models.Model):
    '''
    Model for representing a student.
    '''
    name = models.CharField(
        max_length=100,
        help_text='Enter a name of student.'
    )

    date_birth = models.DateTimeField(
        help_text='Enter a date birth of student.'
    )

    address = models.CharField(
        max_length=50,
        help_text='Enter an address.'
    )

    speciality = models.ForeignKey(
        'Speciality',
        on_delete=models.CASCADE,
    )

    course = models.ManyToManyField(
        'Course'
    )

    def __str__(self):
        '''String for representing the student object.'''
        return self.name


class Speciality(models.Model):
    '''
    Model for representing a Speciality.
    '''
    name = models.CharField(
        max_length=50,
        help_text='Enter an address.'
    )

    description = models.TextField(
        max_length=200,
        help_text='Enter a description of speciality.')

    def __str__(self):
        '''String for representing the Speciality object.'''
        return self.name


class Course(models.Model):
    '''
    Model for representing a course.
    '''
    name = models.CharField(
        max_length=50,
        help_text='Enter a name.'
    )

    speciality = models.ManyToManyField(
        'Speciality',
    )

    description = models.TextField(
        max_length=200,
        help_text='Enter a description of course.')

    professor = models.OneToOneField(
        'Professor',
        on_delete=models.CASCADE,
    )

    instructor = models.ForeignKey(
        'Instructor',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        '''String for representing the Course object.'''
        return self.name


class Professor(models.Model):
    '''
    Model for representing a Professor.
    '''
    name = models.CharField(
        max_length=50,
        help_text='Enter a name.'
    )

    def __str__(self):
        '''String for representing the professor object.'''
        return self.name


class Instructor(models.Model):
    '''
    Model for representing an Instructor.
    '''
    name = models.CharField(
        max_length=50,
        help_text='Enter a name.'
    )

    def __str__(self):
        '''String for representing the instructor object.'''
        return self.name
