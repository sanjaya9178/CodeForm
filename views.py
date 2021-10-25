from django.shortcuts import render, HttpResponse
from .forms import UserForm
from .models import UserItem
from django.http import JsonResponse
# Create your views here.

def item_show(request):
    if request.method=='POST':
        fm=UserForm(request.POST)
    else:
        fm=UserForm()

    return render(request,'itemdisplay.html',{'form':fm})

def ajax_call(request):

    if request.method == 'POST':
        item_no = request.POST.get('data1')
        print('item no',item_no)
        item_details=UserItem.objects.filter(item_number=item_no)
        print(item_details)
        dic = {}
        for x in item_details:
            dic['name'] = x.item_name
            dic['number'] = x.item_number
            dic['quentity'] = x.item_quantity
        print(dic)

    return JsonResponse(dic)
