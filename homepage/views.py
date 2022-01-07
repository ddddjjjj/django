from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Hello World")
    return render(request, 'index.html', {})

def abc(request):
    return render(request, 'jupyter.html',{})

def work(request):
    return render (request, 'test.html',{})