from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def rohit(request):
    return render(request,'rohit.html')
def virat(request):
    return HttpResponse('<h1> chease master </h1>')