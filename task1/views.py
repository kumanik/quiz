from django.shortcuts import redirect, render
import json

from .models import Marks
from .models import Question


def show_all(request):
    content = {}
    content['questions'] = Question.objects.all()
    if request.method == 'POST':
        post_data = json.loads(request.body.decode("utf-8"))
        name = request.session['name']
        roll = request.session['roll']
        result = list()
        marks = 0
        for i in range(len(post_data)):
            qs = Question.objects.get(id=int(post_data[i]['id']))
            corr_no = 0
            for word in post_data[i]['answers']:
                if word == qs.word1.word and qs.word1.correct:
                    corr_no += 1
                elif word == qs.word2.word and qs.word2.correct:
                    corr_no += 1
                elif word == qs.word3.word and qs.word3.correct:
                    corr_no += 1
            if corr_no == 2:
                marks += 1
            result.append({
                'question': str(qs),
                'selected': post_data[i]['answers'],
                'marks': 1 if corr_no == 2 else 0
            })
        with(open('csv/' + 'task1-' + name + roll + '.csv', 'w')) as f:
            f.write('SlNo,Question,SelectedOption,Marks\n')
            for i in range(len(result)):
                selected = ' '.join(elem for elem in result[i]['selected'])
                f.write(str(i) + ',' + result[i]['question'] + ',' + selected
                        + ',' + str(result[i]['marks']) + '\n')
        stud_marks = Marks.objects.filter(name=name, roll=roll)
        if len(stud_marks) == 1:
            stud_marks = stud_marks[0]
            stud_marks.marks = marks
            stud_marks.save()
        else:
            Marks.objects.create(
                csv='csv/' + 'task1-' + name + roll + '.csv',
                total_marks=marks, name=name, roll=roll)
        return redirect('/')

    return render(request, 'task1/task1.html', content)
