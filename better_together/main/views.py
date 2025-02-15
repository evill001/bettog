from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RegistrationForm, ReportForm
from .models import Report, Request, CustomUser
from .forms import RequestForm  # Добавляем форму заявок


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


@login_required
def submit_request(request):
    if request.method == "POST":
        print(f"request.user: {request.user}")  
        print(f"request.user.is_authenticated: {request.user.is_authenticated}")  
        print(f"request.user.id: {request.user.id}")  

        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            new_request = form.save(commit=False)
            new_request.user = request.user  
            print(f"new_request.user перед сохранением: {new_request.user}")  
            new_request.save()
            return redirect("reports")
    else:
        form = RequestForm()
    
    return render(request, "submit_request.html", {"form": form})




@login_required
def create_request(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Чтобы подать заявку, вам нужно войти в аккаунт.")
        return redirect("login")  # Перенаправляем на страницу входа

    if request.method == "POST":
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            request_obj = form.save(commit=False)
            request_obj.user = request.user  # Устанавливаем пользователя перед сохранением
            request_obj.save()
            return redirect("index")  # Перенаправляем после отправки
    else:
        form = RequestForm()

    return render(request, "create_request.html", {"form": form})



@login_required
def profile(request):
    user = CustomUser.objects.get(id=request.user.id)  # Получаем текущего пользователя
    user_requests = Request.objects.filter(user=user).order_by('-created_at')[:4]  # Ограничиваем 4 последними
    return render(request, "profile.html", {"user": user, "user_requests": user_requests})


def index(request):
    latest_requests = Request.objects.order_by('-created_at')[:4]  # Последние 4 заявки
    solved_requests_count = Request.objects.filter(status='Решено').count()  # Количество решённых

    context = {
        'latest_requests': latest_requests,
        'solved_requests_count': solved_requests_count,
    }

    return render(request, 'index.html', context)