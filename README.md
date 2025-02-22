# 📊 WhatsApp Chat Analysis Dashboard 🚀

## 🔥 Overview
This project is a **WhatsApp Chat Analysis Dashboard** built using **Django** as the backend. It features a **secure login system**, **interactive data visualizations with Chart.js**, and **AJAX for dynamic data fetching** without page reloads.

## 🛠️ Features
- 🔐 **User Authentication**: Secure login system for dashboard access.
- 📊 **Interactive Charts**: Uses **Chart.js** for visualizing WhatsApp chat data.
- ⚡ **AJAX Integration**: Fetches chat data dynamically without refreshing the page.
- 📂 **Chat Data Processing**: Extracts insights like **total messages, media shared, most active users, and word frequencies**.
- 📅 **Activity Analysis**: Daily, monthly, and weekly chat trends.
- 😂 **Emoji Usage Insights**: Detects and visualizes emojis used in conversations.

## 🏢 Tech Stack
- **Backend**: Django (Python) 🐍
- **Frontend**: HTML, CSS, JavaScript 🎨
- **Charts**: Chart.js 📊
- **Database**: SQLite / PostgreSQL 👖
- **AJAX**: Fetch chat data dynamically ⚡

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/whatsapp-chat-analysis.git
cd whatsapp-chat-analysis
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations & Run Server
```bash
python manage.py migrate
python manage.py runserver
```
Access the dashboard at **http://127.0.0.1:8000/** 🚀

## 🔐 Login System
- Default credentials:
  - **Username**: `admin`
  - **Password**: `yourpassword`
- To create a new superuser:
  ```bash
  python manage.py createsuperuser
  ```

## 📰 API Endpoint for Chat Data
The chat data is fetched dynamically via AJAX from:


## 📊 Dashboard Features

### ✅ Total Messages, Words, Media & Links Shared
Displays **total chat statistics** in a structured format.

### ✅ Charts & Visualizations
- **Bar Chart**: User-wise message distribution 📊
- **Line Charts**: Daily & monthly activity trends 📈
- **Heatmap**: Weekly activity analysis 🔥
- **Pie Chart**: Emoji distribution 😂

### ✅ Most Active Users
Identifies the top contributors in group chats.

### ✅ Most Common Words
Finds the most frequently used words (excluding stopwords).

## 🚀 Future Enhancements
- 📌 Export chat analysis reports as **PDF**.
- 📌 More **chart types** for deeper insights.
- 📌 Sentiment analysis of messages using **NLP**.

## 💖 Contributing
Feel free to **fork** the repo, **submit issues**, or **contribute**! PRs are always welcome! 🚀

## 🐟 License
This project is licensed under the **MIT License**.

---

🔹 **Made with ❤️ using Django & JavaScript** 🔹

