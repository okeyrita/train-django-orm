from django.urls import path
from . import views


urlpatterns = [
    path('speciality/', views.speciality_page, name='speciality'),
    path('course/', views.course_page, name='course' ),
    path('speciality/<int:spec>', views.details_speciality, name='speciality_details'),
]