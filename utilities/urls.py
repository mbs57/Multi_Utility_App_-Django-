from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Home page with 4 options
    path('calendar/<int:month_offset>/', views.calendar_view, name='calendar_view'),
    path('toggle_task/<int:task_id>/', views.toggle_task, name='toggle_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('task_list/', views.task_list, name='task_list'),
    path('calculator/', views.calculator_view, name='calculator_view'),
    path('alarm/', views.alarm_view, name='alarm_view'),  # Alarm URL
]
