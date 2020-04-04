from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('course_detail/<int:id>', views.course_detail, name='course_detail'),


]
