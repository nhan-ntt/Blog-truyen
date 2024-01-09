from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse('<h1>Blog Home</h1>')

    return render(request, 'index.html')

def counter(request):
    words = request.POST['words']   #name = 'words' in index.html
    lengthOfWords = len(words.split())
    return render(request, 'counter.html', {'length': lengthOfWords, 'words': words})
    
