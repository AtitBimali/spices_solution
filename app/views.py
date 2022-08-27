from ast import In
from tkinter.messagebox import NO
from django.shortcuts import redirect, render,get_object_or_404
from matplotlib.style import context
from .models import *
import requests

from django.db.models import Q

from django.http import HttpResponseRedirect
from . import forms
# Create your views here.

def main(request):
    return render(request,'app/main.html')

def index(request):
    industry_form=forms.Industry()
    if request.method=='POST':
        industry_form=forms.Industry(request.POST)
        if industry_form.is_valid():
            industry_form.save()
    context ={
       'industry_form':industry_form
    }
    return render(request,'app/index.html',context=context)

def register(request):
    if request.method=='POST':
        register_form=forms.Company(request.POST)
        if register_form.is_valid():

            register_form.save()
        return HttpResponseRedirect('/companies')
    register_form = forms.Company()
    context ={
       'register_form':register_form
    }
    return render(request,'app/register.html',context=context)

def company_list(request):
    company_list = Company.objects.all()
    industries = Industry.objects.all()
    industry = request.GET.get('industry')
    if industry == None:
        company_list = Company.objects.all()
    else:
         company_list = Company.objects.filter(industry_type=industry)
    context={
        'industries':industries,
        'company_list':company_list
    }
    return render(request,'app/company_list.html',context=context)

def search_view(request):
    # whatever user write in search box we get in query
    query = request.GET['query']
    print("searched")
    if query:
        companies=Company.objects.filter(Q(company_name__icontains=query) | Q(owner_name__icontains=query) | Q(address__icontains=query))
        word="Searched Result :"
        return render(request,'app/company_list.html',{'companies':companies,'word':word,})