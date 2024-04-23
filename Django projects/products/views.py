from django.shortcuts import render
from django.http import HttpResponse
from .models import products
# Create your views here.
def index(reqest):
    all_products=products.objects.all()
    return render(reqest,'index.html',{'products':all_products})

def new(reqest):
    return HttpResponse('sarah')