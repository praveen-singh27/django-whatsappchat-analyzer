from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  
    path('logout/', views.logout_view, name='logout'),
    path('charts/', views.charts, name='charts'),
    path('tables/', views.tables, name='tables'),
    path('chat-data/', views.chat_data_api, name='chat_data_api'),
    path("get-chat-analysis/", views.get_chat_analysis, name="chat_analysis_api"),
]
