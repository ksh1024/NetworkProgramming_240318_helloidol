from django.http import HttpResponse
from django.shortcuts import render

def say_hello(reguest):
    return HttpResponse("Hello World!")