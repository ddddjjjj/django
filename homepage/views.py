from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Hello World")
    return render(request, 'index.html', {})

def result(request):
    return render(request, 'projeda.html',{})

def work(request):
    return render (request, 'test.html',{})