from django.shortcuts import render
from . models import RegistredCourse
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    ctx = {}
    ctx['registred_course'] =[rc.course for rc in request.user.registredcourse_set.all()]
    return render(request, 'student-profile.html', ctx)
