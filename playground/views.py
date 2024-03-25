from django.http import HttpResponse
from django.shortcuts import render

def say_hello(reguest):
    return HttpResponse("Hello World!")

def say_hello_html(request):
    return render(request, 'playground/hello.html', {'name' : '지우야 ','greeting': '안녕'})

def say_bye_html(request):
    context ={
        'singer' : '아리아나 그란데',
        'title' : 'bye',
    }
    return render(request, 'playground/bye.html', context=context)

