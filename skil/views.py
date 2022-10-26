from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from skil.models import Equestion

# Create your views here.
def index(request):
    return render(request, 'skil/index.html')

def exceltest(request, excel_id):
    try:
        excel = Equestion.objects.get()
    except Equestion.DoesNotExist:
        raise Http404("Wquestion does not exist")
    data = {'excel':excel}
    return render(request, 'skil/excel_test.html', data)

def nettest(request):
    return render(request, 'skil/net_test.html')

def Eanswer(request):
    return render(request, 'skil/Eanswer.html')

def Nanswer(request):
    return render(request, 'skil/Nanswer.html')


def percent(request):
    return render(request, 'skil/parcent.html')