from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji
import os
from django.conf import settings
import re

extract = URLExtract()

def fetch_stats(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # fetch the number of messages
    num_messages = df.shape[0]

    # fetch the total number of words
    words = []
    for message in df['message']:
        words.extend(message.split())

    # fetch number of media messages
    num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]

    # fetch number of links shared
    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))

    return num_messages,len(words),num_media_messages,len(links)

def most_busy_users(df):
    x = df['user'].value_counts().head()
    df = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'name', 'user': 'percent'})
    return x,df

def create_wordcloud(selected_user,df):

    f = open('stop_hinglish.txt', 'r')
    stop_words = f.read()

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    def remove_stop_words(message):
        y = []
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)

    wc = WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    temp['message'] = temp['message'].apply(remove_stop_words)
    df_wc = wc.generate(temp['message'].str.cat(sep=" "))
    return df_wc

def most_common_words(selected_user, df):
    stop_words_path = os.path.join(settings.BASE_DIR, 'dashboard', 'stop_hinglish.txt')
    # Load stop words
    with open(stop_words_path, 'r') as f:
        stop_words = f.read().split()

    # Add 'deleted' to stop words list (to exclude it) or directly add in 'stop_hinglish.txt'
    stop_words.extend(['deleted', 'message'])

    # Filter user-specific messages
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # Remove group notifications and media messages
    temp = df[(df['user'] != 'group_notification') & (df['message'] != '<Media omitted>\n')]

    words = []

    # Extract words
    for message in temp['message']:
        for word in message.lower().split():
            # Keep only words (removes symbols, numbers, etc.)
            if word not in stop_words and re.match(r"^[a-zA-Z]+$", word):
                words.append(word)

    # Get most common words
    most_common_df = pd.DataFrame(Counter(words).most_common(20), columns=['Word', 'Frequency'])
    
    return most_common_df


def emoji_helper(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if emoji.is_emoji(c)])

    emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))

    return emoji_df

def monthly_timeline(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()

    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))

    timeline['time'] = time

    return timeline

def daily_timeline(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    daily_timeline = df.groupby('only_date').count()['message'].reset_index()

    return daily_timeline

def week_activity_map(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['day_name'].value_counts()

def month_activity_map(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['month'].value_counts()

def activity_heatmap(selected_user,df): # Modified 25-02-2025

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    user_heatmap = df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)

    # Convert the heatmap into the required format
    heatmap_data = []
    for day, row in user_heatmap.iterrows():
        for period, count in row.items():
            heatmap_data.append({
                "x": int(period.split('-')[0]),  # Extract numeric hour
                "y": day,  # Day of the week
                "v": int(count)  # Message count
            })

    return heatmap_data















