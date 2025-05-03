from tracker import Tracker
import datetime

#Initialize tracker and database connection
tracker = Tracker()

#Insert sample datas to the database file
#One daily habit and two weekly habits
sample_habits = [
    ("meditation", "daily", datetime.date.today() - datetime.timedelta(days=2), 2, datetime.date.today() - datetime.timedelta(days=1)),
    ("stand-up paddling", "weekly", datetime.date.today() - datetime.timedelta(days=14), 1, datetime.date.today() - datetime.timedelta(days=10)),
    ("yoga", "weekly", datetime.date.today() - datetime.timedelta(days=5), 2, datetime.date.today())
]

#Add each sample habit to the database
for name, htype, created_date, streak, last_checked in sample_habits:
    try:
        tracker.cursor.execute(
            '''
            INSERT OR REPLACE INTO habits (name, type, created_date, current_streak, last_checked)
            VALUES (?, ?, ?, ?, ?)
            ''',
            (
                name,
                htype,
                created_date.isoformat(),
                streak,
                last_checked.isoformat()
            )
        )
    except Exception as e:
        print(f"Error inserting habit {name}: {e}")

tracker.conn.commit()

#Inform user the sample data is inserted
print("Sample data inserted successfully.")
