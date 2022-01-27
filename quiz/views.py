from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        request.session['roll'] = request.POST['roll']
    try:
        print(request.session['roll'])
    except:
        pass
    return render(request, 'index.html')