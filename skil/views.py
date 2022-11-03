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
        excel = Equestion.objects.filter(id__gte=10*excel_id-9).filter(id__lt=10*excel_id+1)
        data = {'excel':excel}
        return render(request, 'skil/excel_test.html', data)
    elif request.method == 'POST':
        ans = request.POST.get('option0', None)
        return HttpResponse('ans: {}'.format(ans))
        

def nettest(request, net_id):
    try:
        net = Equestion.objects.filter(id__gte=10*net_id-9).filter(id__lt=10*net_id+1)
    except Equestion.DoesNotExist:
        raise Http404("excel does not exist")
    data = {'net':net}
    return render(request, 'skil/excel_test.html', data)

def Eanswer(request, excel_id):
    #if request.method == 'GET':
    excel = Equestion.objects.filter(id__gte=10*excel_id-9).filter(id__lt=10*excel_id+1)
    data = {'excel':excel}
    return render(request, 'skil/Eanswer.html', data)

def Nanswer(request):
    return render(request, 'skil/Nanswer.html')

def percent(request):
    return render(request, 'skil/percent.html')