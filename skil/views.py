from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from skil.models import Equestion

from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request, 'skil/index.html')

def esele(request):
    return render(request, 'skil/esele.html')

def nsele(request):
    return render(request, 'skil/nsele.html')

def exceltest(request, excel_id):
    if request.method == 'GET':
        exc = Equestion.objects.filter(id__gte=10*excel_id-9).filter(id__lt=10*excel_id+1)
        paginator = Paginator(exc, 1)
        p = request.GET.get('p')
        excel = paginator.get_page(p)
        data = {'excel':excel}
        return render(request, 'skil/excel_test.html', data)
    elif request.method == 'POST':
        

def nettest(request, net_id):
    try:
        net = Equestion.objects.filter(id__gte=10*net_id-9).filter(id__lt=10*net_id+1)
    except Equestion.DoesNotExist:
        raise Http404("excel does not exist")
    data = {'net':net}
    return render(request, 'skil/excel_test.html', data)

def Eanswer(request):
    return render(request, 'skil/Eanswer.html')

def Nanswer(request):
    return render(request, 'skil/Nanswer.html')

def percent(request):
    return render(request, 'skil/percent.html')