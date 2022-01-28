from django.shortcuts import render

from task2.models import Question

# Create your views here.
def show_all(request):
    context = {}
    context['questions'] = Question.objects.all()
    if request.method == 'POST':
        import json
        post_data = json.loads(request.body.decode("utf-8"))
        name = request.session['name']
        roll = request.session['roll']
        print(post_data)
    return render(request, 'task2/task2.html', context)
