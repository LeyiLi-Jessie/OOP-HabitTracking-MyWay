from habit import Habit
import sqlite3
import datetime

class Tracker:
    def __init__(self):
        #Connect to the SQLite database
        self.conn = sqlite3.connect('habits.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        #Create the habits table if it doesn't already exist
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS habits (
                name TEXT PRIMARY KEY,
                type TEXT,
                created_date TEXT,
                current_streak INTEGER,
                last_checked TEXT
            )
        ''')
        self.conn.commit()

    #Mark a habit as checked off for today
    def check_habit(self, name, checked_today):
        self.cursor.execute('SELECT * FROM habits WHERE name=?', (name,))
        row = self.cursor.fetchone()
        if row:
            habit = Habit(row[0], row[1])
            habit.created_date = datetime.date.fromisoformat(row[2])
            habit.current_streak = row[3]
            habit.last_checked = datetime.date.fromisoformat(row[4]) if row[4] else None
            habit.check_done(checked_today)
            self.cursor.execute('''
                UPDATE habits SET current_streak=?, last_checked=? WHERE name=?
            ''', (habit.current_streak, habit.last_checked.isoformat() if habit.last_checked else None, name))
            self.conn.commit()

    #Add a new habit to the database
    def add_habit(self, name, type):
        habit = Habit(name, type)
        self.cursor.execute('INSERT OR IGNORE INTO habits VALUES (?, ?, ?, ?, ?)',
                            (habit.name, habit.type, habit.created_date.isoformat(), habit.current_streak, habit.last_checked))
        self.conn.commit()

    #Delete a habit from the database
    def delete_habit(self, name):
        self.cursor.execute('DELETE FROM habits WHERE name=?', (name,))
        self.conn.commit()

    #Retrieve all habits from the database
    def list_habits(self):
        self.cursor.execute('SELECT * FROM habits')
        return self.cursor.fetchall()

    #Find the habit with the highest current streak
    def highest_streak(self):
        self.cursor.execute('SELECT name, current_streak FROM habits ORDER BY current_streak DESC LIMIT 1')
        return self.cursor.fetchone()
    
    #Get the current streak of a specific habit
    def streak_of_habit(self, name):
        self.cursor.execute('SELECT current_streak FROM habits WHERE name=?', (name,))
        return self.cursor.fetchone()


