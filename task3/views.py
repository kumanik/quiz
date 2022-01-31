import json
from django.shortcuts import render

from .models import Question

def show_all(request):
    context = {}
    context['questions'] = Question.objects.all()
    if request.method == 'POST':
        post_data = json.loads(request.body.decode("utf-8"))
        print(post_data)
    return render(request, 'task3/task3.html', context)