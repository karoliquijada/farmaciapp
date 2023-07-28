from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


@login_required
def index(request):
     return render(request, "index.html")

def salir(request):
    logout(request)
    return redirect('/')
