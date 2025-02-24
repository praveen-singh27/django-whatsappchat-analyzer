from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  
    path('logout/', views.logout_view, name='logout'),
    path('charts/', views.charts, name='charts'),
    path('tables/', views.tables, name='tables'),
    path('chat-data/', views.chat_data_api, name='chat_data_api'),
    path('get-stats/', views.get_stats, name="get-stats"),
    path('monthly-timeline/', views.monthly_timeline_api, name='monthly-timeline'),
    path('daily-timeline/', views.daily_timeline_api, name='daily-timeline'),
    path('busy-day/', views.busy_day_api, name='busy-day'),
    path('busy-month/', views.busy_month_api, name='busy-month'),

]
