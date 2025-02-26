from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from analysis.models import Customer
import json
from django.http import JsonResponse
from . import preprocess, helper
import pandas as pd
from django.contrib import messages
from .charts import get_monthly_timeline, get_daily_timeline, get_busy_day, get_busy_month, get_weekly_heatmap, get_common_words, get_emoji

def emoji_api(request):
    """API for emoji chart using selected_user from session"""
    emojis = get_emoji(request)
    
    top_emojis = emojis.head(10)

    data = {
        "emoji": top_emojis[0].tolist(),  # X-axis: Weekdays
        "emoji_count": top_emojis[1].tolist()  # Y-axis: Message counts
    }

    return JsonResponse(data,safe=False)


def common_words_api(request):
    """API for most common words chart using selected_user from session"""
    common_words = get_common_words(request)

    # Structure data for JSON response
    data = {
        "word": common_words['Word'].tolist(),  # X-axis: Weekdays
        "word_count": common_words['Frequency'].tolist()  # Y-axis: Message counts
    }
    return JsonResponse(data,safe=False)

    



def weekly_heatmap_api(request):
    """API for weekly heatmap using selected_user from session"""
    selected_user = request.session.get("selected_user", "Overall")  # Default to "Overall"
    chat_data_json = request.session.get("chat_data")
    df = pd.read_json(chat_data_json)

    # ✅ Pass DataFrame to get_busy_month function and pivot table will be returned
    weekly_heatmap = get_weekly_heatmap(selected_user, df)

    return JsonResponse(weekly_heatmap, safe=False)


def busy_month_api(request):
    """API for most busy month chart using selected_user from session"""
    selected_user = request.session.get("selected_user", "Overall")  # Default to "Overall"
    chat_data_json = request.session.get("chat_data")
    df = pd.read_json(chat_data_json)

    # ✅ Pass DataFrame to get_busy_month function
    month_counts = get_busy_month(selected_user, df)
 
    # Structure data for JSON response
    data = {
        "labels": month_counts.index.tolist(),  # X-axis: Weekdays
        "messages": month_counts.values.tolist()  # Y-axis: Message counts
    }
    return JsonResponse(data)


def busy_day_api(request):
    """API for most busy day chart using selected_user from session"""
    selected_user = request.session.get("selected_user", "Overall")  # Default to "Overall"
    chat_data_json = request.session.get("chat_data")
    df = pd.read_json(chat_data_json)
    
    # ✅ Pass DataFrame to get_busy_day function
    week_counts = get_busy_day(selected_user, df) 
    
    # Structure data for JSON response
    data = {
        "labels": week_counts.index.tolist(),  # X-axis: Weekdays
        "messages": week_counts.values.tolist()  # Y-axis: Message counts
    }
    return JsonResponse(data)


def daily_timeline_api(request):
    """API for daily timeline chart using selected_user from session"""
    selected_user = request.session.get("selected_user", "Overall")  # Default to "Overall"
    chat_data_json = request.session.get("chat_data")
    df = pd.read_json(chat_data_json)

    # ✅ Pass DataFrame to timeline function
    timeline_data = get_daily_timeline(selected_user, df) 
    
    # ✅ Structure data for JSON response
    data = {
        "labels": timeline_data["only_date"].tolist(),  # X-axis: Months
        "messages": timeline_data["message_count"].tolist()  # Y-axis: Message counts
    }
    return JsonResponse(data)
    


def monthly_timeline_api(request):
    """API for monthly timeline chart using selected_user from session"""

    # 🟢 Retrieve selected user from session (via context processor)
    selected_user = request.session.get("selected_user", "Overall")  # Default to "Overall"

    # 🟢 Retrieve chat data from session
    chat_data_json = request.session.get("chat_data")

    # ✅ Convert JSON to DataFrame
    df = pd.read_json(chat_data_json)

    # 🔍 Debugging: Print the first few rows
    # print("🚀 Selected User:", selected_user)
    # print("🚀 DataFrame:\n", df.head())
    # print("🚀 Columns:", df.columns)

    # ✅ Pass DataFrame to timeline function which is present in charts.py file
    timeline_data = get_monthly_timeline(selected_user, df)  

    # 🔍 Debugging: Check returned data
    # print("🔍 Timeline Data:\n", timeline_data)
    # print("Timeline Data Type:\n", type(timeline_data))

    # ✅ Structure data for JSON response
    data = {
        "labels": timeline_data["time"].tolist(),  # X-axis: Months
        "messages": timeline_data["message_count"].tolist()  # Y-axis: Message counts
    }
    return JsonResponse(data)

def dashboard(request):
    context = {}

    # Check if chat data exists in session (so that page remains same after refresh)
    chat_data_json = request.session.get("chat_data")
    if chat_data_json:
        df = pd.read_json(chat_data_json)
        users = request.session.get("users", [])
        selected_user = request.session.get("selected_user")
        stats = request.session.get("session_stats", {})

        context.update({
            "users": users,
            "selected_user": selected_user,
        })
        context.update(stats)  # Load stored stats

    response = render(request, 'dashboard/dashboard.html', context)
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
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
        # Case 1: File Upload
        if "chatFile" in request.FILES:
             # ✅ This message is shown only when a file is uploaded
            messages.success(request, " ✅ WhatsApp Chat File Uploaded Successfully! ")

            # Read the uploaded file
            chat_file = request.FILES["chatFile"]
            data = chat_file.read().decode("utf-8")  # Read file content

            df = preprocess.preprocess(data)  # Convert raw chat data into a pandas DataFrame
            request.session["chat_data"] = df.to_json()  # Store uploaded chat data in session

            # Extract unique users
            users = sorted(df["user"].unique().tolist())
            if "group_notification" in users:
                users.remove("group_notification")
            users.insert(0, "Overall")  # Add "Overall" as the first option
            
            # Store the list of users in session so it persists across requests
            request.session["users"] = users  # Store users in session
            context["users"] = users  # Pass users to template

        # Case 2: User selection from dropdown (Not a file upload)
        elif "selected_user" in request.POST:
            # Get the selected user from form data, or fallback to session
            selected_user = request.POST.get("selected_user", request.session.get("selected_user"))
            request.session["selected_user"] = selected_user  # Store selected_user in session

            # Load chat data from session (since no new file was uploaded)
            df = pd.read_json(request.session.get("chat_data"))  # Retrieve session data

            # Fetch chat statistics using helper functions
            num_messages, words, num_media_messages, num_links = helper.fetch_stats(selected_user, df)

            stats = {
                "selected_user": selected_user,
                "total_messages": num_messages,
                "total_words": words,
                "media_shared": num_media_messages,
                "links_shared": num_links,
            }
            
            # Store statistics in session so they persist across page refreshest
            request.session["session_stats"] = stats

            # Retrieve users from session so the dropdown persists
            users = request.session.get("users", [])

            # Update context with stats and user list for rendering
            context.update(stats) 
            context["users"] = users 

    # Case 3: Page refresh - Retrieve stored stats from session (if available)
    elif "session_stats" in request.session:
        # Load statistics from session to maintain state
        context.update(request.session.get("session_stats", {}))
        context["selected_user"] = request.session.get("selected_user", "Overall")  # Default to "Overall"
        context["users"] = request.session.get("users", [])  # Ensure users dropdown persists

    # 🔥 Why isn't the success message appearing when clicking "Show Analysis"?
    # → The message is only added when a file is uploaded (inside `if "chatFile" in request.FILES`).
    # → When selecting a user, a new request is sent, but the success message is not re-added.
    # → Django's default message storage clears messages after the next request-response cycle.

    return render(request, "dashboard/dashboard.html", context)