from django.shortcuts import render
from django.http import HttpResponse

def boult(request):
    return render(request,'boult.html')
def kane(request):
    return HttpResponse('<h1> kane mama </h1>')