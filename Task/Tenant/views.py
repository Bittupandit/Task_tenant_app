# from typing_extensions import Required
from django.shortcuts import redirect, render,get_object_or_404

# Create your views here.

from .models import Tenant
from .forms import TenantForm

def home_page(request):
    qs = Tenant.objects.all().order_by('id')
    context = {'qs':qs}
    return render(request,'main/home_page.html',context)

def create_expenses(request):
    form = TenantForm()
    if request.method == "POST":
        form = TenantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
        else:
            form = TenantForm()
    context = {'form':form}
    return render(request,'main/create_page.html',context)

def update_expenses(request,pk):
    qs = Tenant.objects.get(pk=pk)
    form = TenantForm(instance=qs)
    if request.method == "POST":
        form = TenantForm(request.POST,instance=qs)
        if form.is_valid():
            form.save()
            return redirect('home-page')
        else:
            form = TenantForm()
    context = {'form':form}
    return render(request,'main/update_page.html',context)

def rem_expenses(request,pk):
    qs = get_object_or_404(Tenant,pk=pk)
    qs.delete()
    return redirect('home-page')