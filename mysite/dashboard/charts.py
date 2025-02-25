import pandas as pd
from .helper import monthly_timeline, daily_timeline, week_activity_map, month_activity_map, activity_heatmap, most_common_words, emoji_helper

def get_monthly_timeline(selected_user, df):
    """Fetch monthly timeline data and return formatted DataFrame."""

    # Call the helper function to get the timeline data
    timeline = monthly_timeline(selected_user, df)
    
    # Rename the 'message' column to 'message_count' for consistency
    timeline = timeline.rename(columns={"message": "message_count"})

    # Return the properly formatted DataFrame
    return timeline[['time', 'message_count']]


def get_daily_timeline(selected_user, df):
    """Fetch daily timeline data and return formatted DataFrame."""

    # Call the helper function to get the timeline data
    timeline = daily_timeline(selected_user, df)

    # Ensure 'only_date' is in the correct format
    timeline['only_date'] = pd.to_datetime(timeline['only_date'], unit='ms').dt.date  

    # Rename the 'message' column to 'message_count' for consistency
    timeline = timeline.rename(columns={"message": "message_count"})
   
    return timeline[['only_date', 'message_count']]
    

def get_busy_day(selected_user, df):
    """Fetch most busy day data and return formatted DataFrame."""
    week_counts = week_activity_map(selected_user,df)
    return week_counts

def get_busy_month(selected_user,df):
    """Fetch most busy month data and return formatted DataFrame."""
    month_counts = month_activity_map(selected_user, df)
    return month_counts


def get_weekly_heatmap(selected_user,df):
    """Fetch weekly heatmap data and return formatted DataFrame."""
    weekly_heatmap = activity_heatmap(selected_user,df)
    
    
    return weekly_heatmap

def get_common_words(request):
    """Fetch most common words data and return formatted DataFrame."""
    selected_user = request.session.get("selected_user", "Overall")  # Default to "Overall"
    chat_data_json = request.session.get("chat_data")
    df = pd.read_json(chat_data_json)
    common_words = most_common_words(selected_user, df)

    return common_words

def get_emoji(request):
    """Fetch emoji data and return formatted DataFrame."""
    selected_user = request.session.get("selected_user", "Overall")  # Default to "Overall"
    chat_data_json = request.session.get("chat_data")
    df = pd.read_json(chat_data_json)

    emojis = emoji_helper(selected_user, df)
    print("✅ EMOJIS:\n", emojis)
    return emojis




