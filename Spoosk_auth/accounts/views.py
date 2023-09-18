from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
import json
from django.contrib.auth import login

def signup(request):
    return render(request, 'signup.html', {})


def signup_endpoint(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        response_data = {}

        try:
            user = User(username=username, password=password)
            user.save()

            response_data['result'] = 'Signup user successful!'
            response_data['username'] = user.username
            response_data['password'] = user.password

            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )

        except:
            return JsonResponse({"error": "This username is already taken!"}, status=403)

    else:
        return render(request, 'test.html', {})
