from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from analysis.models import Customer
import json
from django.http import JsonResponse

def dashboard(request):
    response = render(request, 'dashboard/dashboard.html')
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'  # Prevents caching
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'

    return response


def logout_view(request):
    request.session.flush()  # Clears the entire session
    logout(request)  # Logs out the user
    return redirect('login')  # Redirect to login page after logout

def charts(request):
    return render(request, 'dashboard/charts.html')

def chat_data_api(request):
    data = {
        "labels": ["User1", "User2", "User3", "User4", "User5"],
        "messages": [120, 300, 180, 260, 150]
    }
    return JsonResponse(data)


def tables(request):
    return render(request, 'dashboard/tables.html')


def get_chat_analysis(request):
    if request.method == 'POST':
        pass





