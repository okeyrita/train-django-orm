from django.shortcuts import render
from .models import Student, Speciality, Course, Professor, Instructor


def speciality_page(request):
    '''
    Show list of all Specialities. 
    '''
    speciality = Speciality.objects.all()

    return render(request, 'catalog/base_table.html',
                  {'title': 'List of all Specialities', 'items': speciality})


def course_page(request):
    '''
    Show list of all Course. 
    '''
    course = Course.objects.all()

    return render(request, 'catalog/base_table.html',
                  {'title': 'List of all Specialities', 'items': course})


def details_speciality(request, spec):
    '''
    Show details of speciality.
    '''
    students = Student.objects.filter(speciality=spec.id)
    students_num = len(students)
    courses = Course.objects.filter(specialty=spec.id)

    return render(request, 'catalog/details.html',
                  {'title': 'Details of ',
                   'item': spec,
                   'detail_1': courses,
                   'detail_2': students})


def course_details(request, course_item):
    '''
    Show details of course.
    '''
    specialities = Speciality.objects.filter()
    professor = Professor.objects.get(course_item.professor)
    instructor = Instructor.objects.get(course_item.item)
    list_of_students = Students.objects.all().filter(course=course_item)
