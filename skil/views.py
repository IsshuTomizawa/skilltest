from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from skil.models import Equestion, Nquestion, Epercent, Npercent

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
        op_lst=['option0','option1','option2','option3','option4','option5','option6','option7','option8','option9']
        ans_lst=[]
        your_ans=[]
        xs=[0,1,2,3,4,5,6,7,8,9]
        #ans = request.POST.get("option0")
        excel = Equestion.objects.filter(id__gte=10*excel_id-9).filter(id__lt=10*excel_id+1)
        excela = list(excel.values())
        lst=[]
        for ex in excela:
            lst.append(ex["answer"])
        for op in op_lst:
            ans = request.POST.get(op)
            your_ans.append(ans)
        for n in range(10):
            exc=Epercent.objects.get(pk=10*(excel_id-1)+n+1)
            if your_ans[n] == lst[n]:
                ans_lst.append('正解')
                exc.true += 1
                exc.save()
            else:
                ans_lst.append('不正解')
                exc.false += 1
                exc.save()
            exc.percent = (exc.true/(exc.true+exc.false))
            exc.save()
        return render(request, 'skil/Eanswer.html', {'yans':your_ans, 'ans':ans_lst, 'excel':excela, 'xs':xs})
        

def nettest(request, net_id):
    if request.method == 'GET':
        net = Nquestion.objects.filter(id__gte=10*net_id-9).filter(id__lt=10*net_id+1)
        data = {'net':net}
        return render(request, 'skil/net_test.html', data)
    elif request.method == 'POST':
        op_lst=['option0','option1','option2','option3','option4','option5','option6','option7','option8','option9']
        ans_lst=[]
        your_ans=[]
        #ans = request.POST.get("option0")
        net = Nquestion.objects.filter(id__gte=10*net_id-9).filter(id__lt=10*net_id+1)
        neta = list(net.values())
        lst=[]
        for nt in neta:
            lst.append(nt["answer"])
        for op in op_lst:
            ans = request.POST.get(op)
            your_ans.append(ans)
        for n in range(10):
            if your_ans[n] == lst[n]:
                ans_lst.append('正解')     
            else:
                ans_lst.append('不正解')
        return render(request, 'skil/Nanswer.html', {'yans':your_ans, 'ans':ans_lst, 'net':neta})

def Eanswer(request, excel_id):
    #if request.method == 'GET':
    excel = Equestion.objects.filter(id__gte=10*excel_id-9).filter(id__lt=10*excel_id+1)
    data = {'excel':excel}
    return render(request, 'skil/Eanswer.html', data)

def Nanswer(request, net_id):
    net = Nquestion.objects.filter(id__gte=10*net_id-9).filter(id__lt=10*net_id+1)
    data = {'net':net}
    return render(request, 'skil/Nanswer.html', data)

def epercent(request):
    excels = Equestion.objects.all()
    paginator = Paginator(excels, 10) # 1ページに10件表示
    p = request.GET.get('p') # URLのパラメータから現在のページ番号を取得
    excel = paginator.get_page(p) # 指定のページのArticleを取得

    per=Epercent.objects.all()
    paginator = Paginator(per, 10)
    percent = paginator.get_page(p)
    return render(request, 'skil/epercent.html', {'excel': excel, 'p': p, 'percent':percent})
    
def npercent(request):
    nets = Nquestion.objects.all()
    paginator = Paginator(nets, 10) # 1ページに10件表示
    p = request.GET.get('p') # URLのパラメータから現在のページ番号を取得
    net = paginator.get_page(p) # 指定のページのArticleを取得

    per=Npercent.objects.all()
    paginator = Paginator(per, 10)
    percent = paginator.get_page(p)
    return render(request, 'skil/npercent.html', {'net': net, 'p': p, 'percent':percent})