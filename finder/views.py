from django.shortcuts import render
from django.views import generic

from django.views.generic import ListView


# Create your views here.

def index(request):
    return render(request, 'index.html')



    
    
    
   

    
