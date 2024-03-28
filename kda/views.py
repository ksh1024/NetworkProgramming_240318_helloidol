from django.shortcuts import render

# Create your views here.


def show_ari(request):
    return render(request, 'kda/ari.html')

def show_akali(request):
    return render(request, 'kda/akali.html')