from django.contrib import admin

from .models import Marks, Question, Mcq


admin.site.register(Question)
admin.site.register(Mcq)
admin.site.register(Marks)
