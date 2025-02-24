import pandas as pd
from .helper import monthly_timeline

def get_monthly_timeline(selected_user, df):
    """Fetch monthly timeline data and return formatted DataFrame."""

    # Call the helper function to get the timeline data
    timeline = monthly_timeline(selected_user, df)
    print('My Timeline Data')
    # Rename the 'message' column to 'message_count' for consistency
    timeline = timeline.rename(columns={"message": "message_count"})

    # Return the properly formatted DataFrame
    return timeline[['time', 'message_count']]
