import datetime
import sqlite3
from tracker import Tracker
from habit import Habit
import mainfunction
import test_data

def view_habits():
    #Connect to the database file
    conn = sqlite3.connect('habits.db') 
    cursor = conn.cursor()

    #Select all rows from the habits table
    cursor.execute('SELECT * FROM habits')
    habits = cursor.fetchall()

    #Print all habits from the table
    if habits:
        for habit in habits:
            print(f"Name: {habit[0]}, Type: {habit[1]}, Created: {habit[2]}, Streak: {habit[3]}, Last Checked: {habit[4]}")
    else:
        print("No habits found in the database.")

    #Close the connection
    conn.close()

#Clean up the sample data from database
def clear_sample_data(db_name="habits.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM habits")
    conn.commit()
    conn.close()
    print("Database cleaned.")

#Run the function only if this file is executed directly
if __name__ == "__main__":
        view_habits()
        mainfunction.app_menu()
        clear_sample_data()




