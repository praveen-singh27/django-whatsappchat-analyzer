# Django

# WhatsApp Chat Analysis Dashboard

## 📌 Project Overview
This project is a **WhatsApp Chat Analysis Dashboard** built with **Django, Streamlit, and Chart.js**. It allows users to upload their WhatsApp chat files and visualize various statistics, including message trends, user activity, and emoji usage.

## ✨ Features
- 📂 **Upload WhatsApp Chat File** (TXT format)
- 📊 **Data Processing & Analysis**
- 📈 **Visualizations with Chart.js & Matplotlib**
- 🔥 **User Activity Insights** (Most active users, busiest days)
- 🎨 **Word Cloud & Emoji Analysis**
- 📅 **Daily & Monthly Message Trends**
- 🕵️ **Data Filtering by User**

## 🏗️ Tech Stack
- **Backend:** Django (Python), Pandas
- **Frontend:** Streamlit, Chart.js, Bootstrap
- **Data Visualization:** Matplotlib, Seaborn

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/whatsapp-chat-analysis.git
cd whatsapp-chat-analysis
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Django Server
```bash
python manage.py runserver
```

### 5️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

## 🛠️ How to Use
1. **Upload your WhatsApp chat file** via the Streamlit interface.
2. Select a user to analyze (or choose "Overall").
3. View various analytics, including:
   - **Total Messages, Words, Media, Links**
   - **Most Active Users & Message Trends**
   - **Activity Heatmap**
   - **Emoji Analysis**
4. **Charts Update Dynamically** with data from Django API.

## 📜 API Endpoints
| Endpoint       | Method | Description |
|---------------|--------|-------------|
| `/chat-data/` | GET    | Returns processed chat data as JSON |
| `/charts/`    | GET    | Renders the Chart.js dashboard |

## 📸 Screenshots
_(Add screenshots of your dashboard UI here)_

## 📌 Future Enhancements
- 📊 **More Chart Types** (Pie, Line, Histogram)
- 📥 **Export Reports** (CSV/PDF)
- 🤖 **Sentiment Analysis**
- 📡 **Live Data Updates**

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.

## 📜 License
This project is open-source and available under the **MIT License**.

---
### 📧 Contact
💡 If you have any questions, feel free to reach out!

📩 Email: yourname@example.com  
🔗 GitHub: [github.com/yourusername](https://github.com/yourusername)



