from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from analysis.models import Customer
import json
from django.http import JsonResponse
from . import preprocess, helper
import pandas as pd
from django.contrib import messages

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
        "messages": [700, 300, 300, 260, 150]
    }
    return JsonResponse(data)


def tables(request):
    return render(request, 'dashboard/tables.html')


def get_stats(request):
    context = {}  # Dictionary to store data for Jinja2 template

    if request.method == "POST":
        if "chatFile" in request.FILES:
            messages.success(request, " ✅ WhatsApp Chat File Uploaded Successfully!")
            # Handle file upload
            chat_file = request.FILES["chatFile"]
            data = chat_file.read().decode("utf-8")  # Read file content

            df = preprocess.preprocess(data)  # Convert raw chat data into a pandas DataFrame
            request.session["chat_data"] = df.to_json()  # Store in session (Avoid DB)

            # Extract unique users
            users = sorted(df["user"].unique().tolist())
            if "group_notification" in users:
                users.remove("group_notification")
            users.insert(0, "Overall")  # Add "Overall" as the first option

            request.session["users"] = users  # Store users in session
            context["users"] = users  # Pass users to template

        elif "selected_user" in request.POST:
            # Handle user selection from dropdown
            selected_user = request.POST["selected_user"]
            df = pd.read_json(request.session.get("chat_data"))  # Retrieve session data

            # Fetch chat statistics using helper functions
            num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)

            # Retrieve users from session so dropdown persists
            users = request.session.get("users", [])

            context.update({
                "selected_user": selected_user,
                "users": users,  # Ensure users dropdown is retained
                "total_messages": num_messages,
                "total_words": words,
                "media_shared": num_media_messages,
                "links_shared": num_links,
            })

    return render(request, "dashboard/dashboard.html", context)