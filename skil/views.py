from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request, 'skil/index.html')
    elif request.method == 'POST':
        age = request.POST['age']
        return HttpResponse('age: {}'. format(age))

def wordtest(request):
    data = {
        'question': ['1 + 1 = ?', '1 + 2 = ?']
    }
    return render(request, 'skil/word_test.html', data)

def exceltest(request):
    data = {
        'question': ['1 + 3 = ?', '1 + 4 = ?']
    }
    return render(request, 'skil/excel_test.html', data)

def percent(request):
    if request.method == 'GET':
        return render(request, 'skil/percent.html')
    elif request.method == 'POST':
        return HttpResponse('まだ')