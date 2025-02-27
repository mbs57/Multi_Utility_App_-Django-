# Multi-Utility Django App

A versatile Django application providing multiple functionalities including a **To-Do List**, **Calendar**, **Calculator**, and **Alarm**. The application is designed to help users manage their tasks, check the calendar, perform quick calculations, and set alarms.

## Features

- **To-Do List**: Manage tasks with the ability to add, view, update, and delete tasks. Tasks can be marked as completed.
- **Calendar**: View and navigate through a monthly calendar. View the current month and move between previous and next months.
- **Calculator**: A simple calculator to perform arithmetic operations (Addition, Subtraction, Multiplication, Division).
- **Alarm**: Set an alarm at a specific time, and the application will alert you when the set time arrives.

## Technologies Used

- **Python**: Version 3.8 or higher
- **Django**: Version 5.x
- **HTML/CSS**: For creating user interfaces
- **JavaScript**: For clock and alarm functionalities
- **SQLite**: For database (default in Django)
- **Git**: Version control

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/mbs57/Multi_Utility_App_-Django-.git
cd Multi_Utility_App_-Django-
```
## 2. Create a Virtual Environment

To create a virtual environment, run the following command in your terminal:

```bash
python -m venv env
```
### 3. Activate the Virtual Environment

- On **Windows**:

```bash
.\env\Scripts\activate
```
### 4. Install Dependencies

```bash
pip install -r requirements.txt
```
### 5. Apply Migrations

```bash
python manage.py migrate
```
### 6. Run the Development Server

```bash
python manage.py runserver
```
Once the server is running, visit http://127.0.0.1:8000/ in your browser.

## How to Use

1. **To-Do List**: 
   - Add new tasks with a title, description, and due date.
   - Mark tasks as completed or delete them.
  
2. **Calendar**: 
   - View the calendar for the current month.
   - Navigate to the previous and next months.
  
3. **Calculator**: 
   - Perform simple arithmetic operations like addition, subtraction, multiplication, and division.

4. **Alarm**:
   - Set an alarm by choosing the hour and minute.
   - The alarm will alert you once the set time is reached.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and create a pull request. Please make sure to follow the [coding standards](https://www.python.org/dev/peps/pep-0008/) and write meaningful commit messages.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
