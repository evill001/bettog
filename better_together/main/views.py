from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def reports(request):
    return render(request, 'reports.html')

def report(request):
    return render(request, 'report.html')

def login_view(request):
    return render(request, 'vhod.html')

def register(request):
    return render(request, 'register.html')

def profile(request):
    return render(request, 'profile.html')