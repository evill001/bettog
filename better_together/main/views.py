from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RegistrationForm, ReportForm
from .models import Report
from .forms import RequestForm  # Добавляем форму заявок
from .models import Request


def index(request):
    return render(request, 'index.html', {'user': request.user})

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


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)  # Автоматически логиним пользователя после регистрации
            return redirect("index")  # Перенаправляем на главную страницу
    else:
        form = RegistrationForm()

    return render(request, "register.html", {"form": form})


def submit_request(request):
    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user  # Если заявки привязаны к пользователю
            report.save()
            return redirect("reports")  # Перенаправляем на страницу с заявками
    else:
        form = ReportForm()

    return render(request, "submit_request.html", {"form": form})  # <--- Тут форма передаётся!


@login_required
def create_request(request):
    if not request.user.is_authenticated:
            messages.warning(request, "Чтобы подать заявку, вам нужно войти в аккаунт.")
            return redirect("login")  # Перенаправляем на страницу входа

    if request.method == "POST":
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            request_obj = form.save(commit=False)
            request_obj.save()
            return redirect("index")  # Перенаправляем после отправки
    else:
        form = RequestForm()

    return render(request, "create_request.html", {"form": form})