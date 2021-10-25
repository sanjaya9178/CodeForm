from django.shortcuts import render, HttpResponse
from .forms import UserForm
# Create your views here.

def item_show(request):
    if request.method=='POST':
        fm=UserForm(request.POST)
    else:
        fm=UserForm()

    return render(request,'itemdisplay.html',{'form':fm})

def ajax_call(request):
    if request.method == 'POST':
        item_no = request.POST.get('data')
        print('iteam no',item_no)

    return HttpResponse('success')
