from django.shortcuts import render
from .models import ChaiVariety
from django.shortcuts import get_object_or_404

# Create your views here.
def testing(request):
    chais = ChaiVariety.objects.all()
    return render(request,'main.html',{"chais":chais})

def chai_detail(request,chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request,"chai_details.html",{"chai":chai})

