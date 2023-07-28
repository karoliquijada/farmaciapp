from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "registration/login.html")

@login_required
def dashboard(request):
    return render(request, "dashboard.html")
