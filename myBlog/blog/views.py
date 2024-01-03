from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse('<h1>Blog Home</h1>')
    dic = {
        'name': 'nhon', 
        'quote': 'gambatte'
    }
    return render(request, 'index.html', dic)
    
