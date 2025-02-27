from django.shortcuts import render, redirect
from .models import Task
import calendar
from datetime import datetime
import time

def home_view(request):
    return render(request, 'utilities/home.html')

def task_list(request):
    # Handle form submission (POST request)
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        due_date = request.POST['due_date']
        completed = 'completed' in request.POST  # Check if the checkbox was checked
        
        # Save the task to the database
        task = Task.objects.create(
            title=title,
            description=description,
            due_date=due_date,
            completed=completed
        )
        return redirect('task_list')  # Redirect to refresh the page and show new task

    # For GET request, fetch all tasks to display
    tasks = Task.objects.all()  # Ensure the tasks are fetched correctly
    return render(request, 'utilities/task_list.html', {'tasks': tasks})
def toggle_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed  # Toggle the completion status
    task.save()  # Save the updated task
    return redirect('task_list')  # Redirect to the task list page to refresh
 
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)  # Find the task by ID
    task.delete()  # Delete the task
    return redirect('task_list')  # Redirect to the task list page


from datetime import datetime
import calendar

def calendar_view(request, month_offset=0):
    current_date = datetime.now()
    current_day = current_date.day  # Get today's day

    target_month = current_date.month + month_offset
    target_year = current_date.year

    # Adjust if month exceeds 12 or goes below 1
    if target_month > 12:
        target_month = 1
        target_year += 1
    elif target_month < 1:
        target_month = 12
        target_year -= 1

    cal = calendar.Calendar(firstweekday=6)  # Start the week on Sunday
    month_days = cal.monthdayscalendar(target_year, target_month)

    month_name = calendar.month_name[target_month]

    # Pass the current_day to the template for comparison
    return render(request, 'utilities/calendar.html', {
        'month_days': month_days,
        'month_name': month_name,
        'target_year': target_year,
        'target_month': target_month,
        'current_day': current_day,  # Pass today's day
    })

# Calculator View
def calculator_view(request):
    if request.method == "POST":
        # Get the input values from the form
        num1 = float(request.POST.get('num1', 0))
        num2 = float(request.POST.get('num2', 0))
        operation = request.POST.get('operation', '+')
        
        # Perform the calculation based on the operation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Cannot divide by zero"
        else:
            result = "Invalid operation"
        
        # Render the calculator page with the result
        return render(request, 'utilities/calculator.html', {'result': result})

    return render(request, 'utilities/calculator.html')  # Render the calculator template without result

# Alarm View
def alarm_view(request):
    current_time = datetime.now().strftime("%H:%M:%S")  # Get current time in HH:MM:SS format
    alarm_time = None

    if request.method == "POST":
        alarm_hour = request.POST.get('hour')
        alarm_minute = request.POST.get('minute')

        # Set alarm time
        alarm_time = f"{alarm_hour}:{alarm_minute}:00"

        # Check if the current time matches the alarm time
        while True:
            current_time_check = datetime.now().strftime("%H:%M:%S")
            if current_time_check == alarm_time:
                return render(request, 'utilities/alarm.html', {'alarm_triggered': True, 'current_time': current_time, 'alarm_time': alarm_time})
            time.sleep(1)  # Sleep for 1 second before checking again

    return render(request, 'utilities/alarm.html', {'current_time': current_time, 'alarm_triggered': False, 'alarm_time': alarm_time})


