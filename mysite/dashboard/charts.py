import pandas as pd
from .helper import monthly_timeline, daily_timeline, week_activity_map

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
    print("Week Counts Data: \n", week_counts)
    return week_counts