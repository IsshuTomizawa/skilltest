from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'skil/index.html')


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

def Eanswer(request):
    return render(request, 'skil/Eanswer.html')

def Wanswer(request):
    return render(request, 'skil/Wanswer.html')

def parcent(request):
    return render(request, 'skil/parcent.html')