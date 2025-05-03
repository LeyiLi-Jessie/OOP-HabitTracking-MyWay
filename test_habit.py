import unittest
import os
import datetime
import sqlite3
from habit import Habit
from tracker import Tracker

class TestHabit(unittest.TestCase):

    #Class method to be run before each test
    #Setting up cls.test_db and cls.tracker for all following methods
    @classmethod
    def setUpClass(cls):
        cls.test_db = "habits.db"
        cls.tracker = Tracker()

    #Test the method to add a new  habit
    def test_add_daily_habit(self):
        self.tracker.add_habit("test_habit", "daily")
        self.tracker.cursor.execute("SELECT * FROM habits WHERE name=?", ("test_habit",))
        row = self.tracker.cursor.fetchone()
        self.assertIsNotNone(row)
        self.assertEqual(row[0], "test_habit")
        self.assertEqual(row[1], "daily")
        self.assertEqual(row[3], 0)  #Streak is set to be 0 by default
        self.assertEqual(row[4], None) #Date of last check is set to be None by default

    #Test the method to list all habits from database file
    def test_list_habits(self):
        self.tracker.add_habit("reading", "daily")
        self.tracker.add_habit("meditation", "weekly")
        habits = self.tracker.list_habits()
        habit_names = [h[0] for h in habits]
        self.assertIn("reading", habit_names)
        self.assertIn("meditation", habit_names)

    #Test the method to delete a habit
    def test_delete_habit(self):
        self.tracker.add_habit("exercise", "daily")
        self.tracker.delete_habit("exercise")
        habits = self.tracker.list_habits()
        habit_names = [h[0] for h in habits]
        self.assertNotIn("exercise", habit_names)

    #Test the method to check a daily habit as done for today
    def test_check_off_daily_streak_increment(self):
        habit = Habit("exercise", "daily")
        habit.last_checked = datetime.date.today() - datetime.timedelta(days=1)
        habit.current_streak = 1
        habit.check_done(True)
        self.assertEqual(habit.current_streak, 2)

    #Test the method to re-count the daily habit streak from 1 if the daily habit is not consecutively checked within 1 day
    def test_check_off_daily_streak_reset(self):
        habit = Habit("exercise", "daily")
        habit.last_checked = datetime.date.today() - datetime.timedelta(days=2)
        habit.current_streak = 3
        habit.check_done(True)
        self.assertEqual(habit.current_streak, 1)

    #Test the method to check a weekly habit as done for today
    def test_check_off_weekly_streak_increment(self):
        habit = Habit("yoga", "weekly")
        habit.last_checked = datetime.date.today() - datetime.timedelta(days=6)
        habit.current_streak = 2
        habit.check_done(True)
        self.assertEqual(habit.current_streak, 3)

    #Test the method to re-count the weekly habit streak from 1 if the weekly habit is not consecutively checked within 7 day
    def test_check_off_weekly_streak_reset(self):
        habit = Habit("yoga", "weekly")
        habit.last_checked = datetime.date.today() - datetime.timedelta(days=10)
        habit.current_streak = 4
        habit.check_done(True)
        self.assertEqual(habit.current_streak, 1)

    #Test the method does not allow re-counting streak within one day
    def test_avoid_exploitation (self):
        habit = Habit("meditation", "daily")
        habit.last_checked = datetime.date.today()
        habit.current_streak = 5
        habit.check_done(True)
        self.assertEqual(habit.current_streak, 5)

    #Test the streak is not increased if the user selects that the habit is not finished today
    def test_check_not_done(self):
        habit = Habit("meditation", "daily")
        habit.current_streak = 4
        habit.check_done(False)
        self.assertEqual(habit.current_streak, 0)
        self.assertIsNone(habit.last_checked)

    #Test the method of giving the user the highest streak currently in the database among all habits
    def test_highest_streak(self):
        self.tracker.add_habit("running", "daily")
        self.tracker.add_habit("yoga", "weekly")
        #Providing predefined streaks for testing
        self.tracker.cursor.execute(
            "UPDATE habits SET current_streak=? WHERE name=?", (2, "running")
        )
        self.tracker.cursor.execute(
            "UPDATE habits SET current_streak=? WHERE name=?", (5, "yoga")
        )
        self.tracker.conn.commit()
        #Getting the highest streak by the method defined in Tracker class
        top = self.tracker.highest_streak()
        self.assertEqual(top[0], "yoga")
        self.assertEqual(top[1], 5)

    #Test the method of showing the streak of a specified habit
    def test_streak_of_habit(self):
        self.tracker.add_habit("test_habit2", "daily")
        #Set a pre-defined streak for testing purpose
        self.tracker.cursor.execute(
            "UPDATE habits SET current_streak=? WHERE name=?", (4, "test_habit2")
        )
        self.tracker.conn.commit()
        streak = self.tracker.streak_of_habit("test_habit2")
        #The returned streak is a tuple by default, so we take the first element which is the streak as an integer for the test
        self.assertEqual(streak[0], 4)

    #Clean up the database after each test to avoid contamination of test
    @classmethod
    def tearDownClass(cls):
        cls.tracker.conn.close()
        os.remove(cls.test_db)

#Tests should only be run when the file run directly
if __name__ == '__main__':
    unittest.main()
