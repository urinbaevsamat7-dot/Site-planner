from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Task
import random

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        login(request, user)
        return redirect('home')
    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def create_plan(request):
    if request.method == 'POST':
        tasks = request.POST.getlist('tasks')
        for t in tasks:
            if t.strip():
                Task.objects.create(user=request.user, text=t)
        return redirect('plan')
    return render(request, 'create_plan.html')

@login_required
def plan(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'plan.html', {'tasks': tasks})

@login_required
def chat_page(request):
    return render(request, 'chat.html')

def chatbot(request):
    msg = (request.GET.get('message') or "").lower()

    # ответы
    if "привет" in msg or "сәлем" in msg:
        return JsonResponse({
            "reply": "Отличное начало 😎 Готовы сделать план на день?"
        })

    elif "план" in msg:
        return JsonResponse({
            "reply": "Попробуй разбить день на 3 блока: утро (важные задачи), день (учёба/работа), вечер (отдых)."
        })

    elif "совет" in msg:
        tips = [
            "Начни с 3 главных задач на день 🎯",
            "Используй правило 2 минут — делай сразу мелкие задачи",
            "Не перегружай себя, максимум 5–7 задач в день",
            "Делай перерывы каждые 60–90 минут ⏳",
            "Сначала сложное, потом лёгкое 💪"
        ]
        return JsonResponse({
            "reply": random.choice(tips)
        })

    elif "как" in msg and "план" in msg:
        return JsonResponse({
            "reply": "Сначала запиши всё, что нужно сделать, потом выдели приоритеты и распредели по времени."
        })

    else:
        return JsonResponse({
            "reply": random.choice([
                "🤔 Не совсем понял, попробуй спросить про план или советы",
                "Можешь спросить: 'советы по планировке дня'",
                "Я пока учусь 😅 но могу помочь с планом дня"
            ])
        })