# HabitTracker-MyWay
Welcome to the Habit Tracker "MyWay", which is a command-line habit tracking app built with Python,following object-orietend programming principles and using persistent data storage.\
User of the app can create daily or weekly habits, mark them as done, and track the consistency via streaks.

# Features
- Pre-defined habits + custom habits
- Track both **daily** and **weekly** habits
- Analysis of habit tracking data
- Data stored persistenly via SQLite

# Project Structure
1.habit.py: defines the “Habit” class and encapsulates habit-specific logic such as streak counting and type handling (daily habit vs. weekly habit).\
2.tracker.py:implements the “Tracker” class, handles database initialization, schema setup, and connection management using SQLite, responsible for interfacing with the database and coordinating updates to the database based on user actions.\
3.mainfunction.py:acts as the command-line interface (CLI), offering an interactive menu to users.

# Usage
- Installaion: \
git clone https://github.com/LeyiLi-Jessie/OOP-HabitTracking-MyWay.git 
- Requirements: \
pip install -r Requirements.txt 
- Using the app MyWay:\
python mainfunction.py\
When the app is running, a menu with 7 options will be printed out.\
To exit the app, please select option 7 from the menu.

# Instruction for testing
pip install pytest
- To test the code using pytest\
python test_habit.py
- To test using the app with sample data\
python test.py
(test_data.py is called automatically by test.py to import examplary data into the database file)

# License
This project is licensed under the MIT License.
