from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'my_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('course_detail/<int:id>', views.course_detail, name='course_detail'),
    path('register-course/<int:course_id>', views.register_course, name='register-course'),

]
