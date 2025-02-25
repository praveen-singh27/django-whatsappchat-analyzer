# FOR ANDROID DEVICES
'''
import re
import pandas as pd

def preprocess(data):
    pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'

    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    df = pd.DataFrame({'user_message': messages, 'message_date': dates})
    # convert message_date type
    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%Y, %H:%M - ')

    df.rename(columns={'message_date': 'date'}, inplace=True)

    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:  # user name
            users.append(entry[1])
            messages.append(" ".join(entry[2:]))
        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)

    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    return df

'''

#  IOS USERS
import re
import pandas as pd

def preprocess(data):
    # ✅ Regex pattern for iPhone WhatsApp format
    pattern = r'\[(\d{2}/\d{2}/\d{2}), (\d{2}:\d{2}:\d{2})\] (.*?): (.*)'

    # Extract data using regex
    matches = re.findall(pattern, data)

    if not matches:
        raise ValueError("❌ No valid messages found. Check chat format!")

    # Convert extracted data into DataFrame
    df = pd.DataFrame(matches, columns=['date', 'time', 'user', 'message'])

    # ✅ Combine 'date' and 'time' into a single datetime column
    df['datetime'] = pd.to_datetime(df['date'] + ' ' + df['time'], format='%d/%m/%y %H:%M:%S')

    # ✅ Drop unnecessary columns
    df.drop(columns=['date', 'time'], inplace=True)

    # ✅ Handle system messages & media messages
    df['user'] = df['user'].replace("", "system_notification")
    df['message'] = df['message'].replace(["‎image omitted", "‎sticker omitted", "‎video omitted"], "[Media]")

    # ✅ Extract useful date components
    df['only_date'] = df['datetime'].dt.date
    df['year'] = df['datetime'].dt.year
    df['month_num'] = df['datetime'].dt.month
    df['month'] = df['datetime'].dt.month_name()
    df['day'] = df['datetime'].dt.day
    df['day_name'] = df['datetime'].dt.day_name()
    df['hour'] = df['datetime'].dt.hour
    df['minute'] = df['datetime'].dt.minute

    # ✅ Define time periods (e.g., "14-15" for 2-3 PM)
    df['period'] = df['hour'].apply(lambda h: f"{h}-{h+1 if h < 23 else 0}")

    return df


