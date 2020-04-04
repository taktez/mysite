from django.shortcuts import render
from django.urls import reverse
from my_app.models import Course
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def index(request):
    ctx = {}
    ctx['courses'] = Course.objects.all()
    return render(request, 'index.html', ctx)


def course_detail(request, id):
    ctx = {}
    ctx['course'] = Course.objects.get(id=id)
    ctx['courses'] = Course.objects.all().exclude(id=id)
    return render(request, 'course_detail.html', ctx)


@login_required
def register_course(request, course_id):
    course = Course.objects.get(id=course_id)
    if course not in [rc.course for rc in request.user.registredcourse_set.all()]:
        request.user.registredcourse_set.create(course=course)
    return HttpResponseRedirect(reverse('app_accounts:profile'))
