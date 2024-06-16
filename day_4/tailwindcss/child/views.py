from django.shortcuts import render
from .models import ChaiVariety,Store
from django.shortcuts import get_object_or_404
from .forms import ChaiVarietyForm 

# Create your views here.
def testing(request):
    chais = ChaiVariety.objects.all()
    return render(request,'main.html',{"chais":chais})

def chai_detail(request,chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request,"chai_details.html",{"chai":chai})

def chai_store_view(request):
    stores = None 
    if request.method == "POST":
        form = ChaiVarietyForm(request.POST)
        if form.is_valid():
            chai_varity = form.cleaned_data['chai_varity']
            stores = Store.objects.filter(chai_varieties=chai_varity)
    else:
        form = ChaiVarietyForm()       
      
    return render(request, 'chai_stores.html',{'stores':stores,'form':form})