from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
import json
from django.contrib.auth import login
import random


def signup(request):
    return render(request, 'signup.html', {})


# обработка запроса на регистрацию
def signup_endpoint(request):
    if request.method == 'POST':
        username = f'{random.randrange(10000000000)}'
        usermail = request.POST.get('usermail')
        password = request.POST.get('password')
        if User.objects.filter(email=usermail).exists():
            return JsonResponse({"error": "User with such email address already exists!"}, status=403)
        else:
            user = User(username=username, password=password, email=usermail)
            user.save()
            return JsonResponse({"success": "Check your email to finish registration!"}, status=200)
    else:
        return render(request, 'test.html', {})


# аутентификация пользователя по мейлу
def authenticate_user(email, password):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return None
    else:
        if user.check_password(password):
            return user
    return None


# обработка запроса на авторизацию
def login_endpoint(request):
    if request.method == 'POST':
        user_mail = request.POST.get('user_mail')
        login_password = request.POST.get('login_password')
        user = authenticate_user(user_mail, login_password)
        if user is not None:
            login(request, user)
            return JsonResponse({"success": "The user was log in!"}, status=200)
        else:
            return JsonResponse({"error": "There is no user with such credentials!"}, status=403)
    else:
        return render(request, 'test.html', {})
