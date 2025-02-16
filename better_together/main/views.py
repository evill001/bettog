from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RegistrationForm
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
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            new_request = form.save(commit=False)
            new_request.user = request.user  
            new_request.photo_before = form.cleaned_data.get("photo_before")  # Фотография падает в "до"
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

    if request.user.is_staff:  
        user_requests = Request.objects.all().order_by('-created_at')  # Админ видит ВСЕ заявки
    else:
        user_requests = Request.objects.filter(user=user).order_by('-created_at')  # Обычный юзер – только свои

    return render(request, "profile.html", {"user": user, "user_requests": user_requests})


def index(request):
    latest_requests = Request.objects.order_by('-created_at')[:4]  # Последние 4 заявки
    solved_requests_count = Request.objects.filter(status='Решено').count()  # Количество решённых

    context = {
        'latest_requests': latest_requests,
        'solved_requests_count': solved_requests_count,
    }

    return render(request, 'index.html', context)


@login_required
def reports(request):
    user_requests = Request.objects.filter(user=request.user)  # Все заявки пользователя
    return render(request, "reports.html", {"requests": user_requests})


@login_required
def delete_request(request, request_id):
    request_obj = get_object_or_404(Request, id=request_id)

    if request.user.is_staff:  # Только админ может удалять заявки
        request_obj.delete()
        messages.success(request, "Заявка успешно удалена!")
    else:
        messages.error(request, "У вас нет прав на удаление этой заявки.")

    return redirect("profile")  # Перенаправляем обратно в личный кабинет

@login_required
def update_request_status(request, request_id):
    request_obj = get_object_or_404(Request, id=request_id)

    if request.user.is_staff:  # Проверяем, что это админ
        new_status = request.POST.get("status")

        if new_status == "Решена" and not request_obj.photo_after:
            messages.error(request, "Нельзя установить статус 'Решена' без фото 'После'.")
        elif request_obj.status not in ["Решена", "Отклонена"]:  # Только если заявка не закрыта
            request_obj.status = new_status
            request_obj.save()
            messages.success(request, "Статус заявки обновлён!")
        else:
            messages.error(request, "Нельзя изменить статус завершённой заявки.")
    else:
        messages.error(request, "У вас нет прав на изменение статуса.")

    return redirect("profile")


@login_required
def upload_after_photo(request, request_id):
    if request.method == "POST" and request.user.is_staff:
        request_obj = get_object_or_404(Request, id=request_id)
        if 'photo_after' in request.FILES:
            request_obj.photo_after = request.FILES['photo_after']
            request_obj.save()
    return redirect('profile')