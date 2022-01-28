from django.shortcuts import render

from .models import Question


def show_all(request):
    content = {}
    content['questions'] = Question.objects.all()
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'task1/task1.html', content)
