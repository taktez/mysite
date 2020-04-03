from django.shortcuts import render
from my_app.models import Course


def index(request):
    ctx = {}
    ctx['courses'] = Course.objects.all()
    return render(request, 'index.html', ctx)


def course_detail(request, id):
    ctx = {}
    ctx['course'] = Course.objects.get(id=id)
    ctx['courses'] = Course.objects.all().exclude(id=id)
    return render(request, 'course_detail.html', ctx)