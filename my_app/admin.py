from django.contrib import admin

from . models import (
    Course,
    CourseSession,
    CourseSessionExercise,
    AttachmentFiles,
)


admin.site.register(Course)
admin.site.register(CourseSession)
admin.site.register(CourseSessionExercise)
admin.site.register(AttachmentFiles)