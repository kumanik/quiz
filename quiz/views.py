from django.shortcuts import render


def index(request):
    roll = None
    name = None
    show = False
    if request.method == 'POST':
        request.session['roll'] = request.POST['roll']
        request.session['name'] = request.POST['name']
    try:
        if request.session['roll']:
            show = True
            roll = request.session['roll']
        if request.session['name']:
            show = True
            name = request.session['name']
    except:
        show = False
    return render(request, 'index.html', {'show': show, 'roll': roll, 'name': name})
