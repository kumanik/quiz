from django.contrib import admin

from .models import Marks, Word, Question


admin.site.register(Marks)
admin.site.register(Question)
admin.site.register(Word)
