from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.

def index(request):
    # return HttpResponse('<h1>Blog Home</h1>')

    features = Feature.objects.all()

    return render(request, 'index.html', {'features': features})

def counter(request):
    words = request.POST['words']   #name = 'words' in index.html
    lengthOfWords = len(words.split())
    return render(request, 'counter.html', {'length': lengthOfWords, 'words': words})
    
