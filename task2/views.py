from django.shortcuts import redirect, render

from task2.models import Marks, Question

# Create your views here.


def show_all(request):
    context = {}
    context['questions'] = Question.objects.all()
    if request.method == 'POST':
        import json
        post_data = json.loads(request.body.decode("utf-8"))
        name = request.session['name']
        roll = request.session['roll']
        result = list()
        marks = 0
        for i in range(len(post_data)):
            qs = Question.objects.get(id=int(post_data[i]['id']))
            result.append({
                'question': qs.question_text,
                'option': post_data[i]['selected'],
                'marks': 1 if post_data[i]['selected'] == qs.correct_option else 0
            })
            marks += 1 if post_data[i]['selected'] == qs.correct_option else 0
        with open('csv/' + name + roll + '.csv', 'w') as f:
            f.write('SlNo,Question,Option,Marks\n')
            for i in range(len(result)):
                f.write(str(i) + ',' + result[i]['question'] + ',' + result[i]
                        ['option'] + ',' + str(result[i]['marks']) + '\n')

        stud_marks = Marks.objects.filter(name=name, roll=roll)
        if(len(stud_marks) == 1):
            stud_marks = stud_marks[0]
            stud_marks.marks = marks
            stud_marks.save()
        else:
            Marks.objects.create(
                csv='csv/' + name + roll +
                '.csv', total_marks=marks, name=name, roll=roll)
        return redirect('/')

    return render(request, 'task2/task2.html', context)
