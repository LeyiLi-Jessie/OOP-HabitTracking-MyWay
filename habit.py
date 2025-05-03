import datetime

class Habit:
    def __init__(self, name, type):
        #Limits the possible type to be either daily or weekly
        if type not in ("daily", "weekly"):
            raise ValueError (f"Invalid type '{type}'. Type must be 'daily' or 'weekly'.")

        #Initialize the habit with its name, creation date, and streak data
        self.name = name
        self.type = type
        self.created_date = datetime.date.today()
        self.current_streak = 0
        self.last_checked = None

    #Method to mark the habit as done for today
    def check_done (self,checked_today):
        today = datetime.date.today()

        #Avoid code being exploited: if already checked once today, no need to update again
        if self.last_checked == today:
            return

        #For the situation when the user says that the habit has been done for today
        #Namely, checked_today is yes
        if checked_today:

            #Applicable for new habit - current_streak is None by default
            if self.last_checked is None: 
                self.current_streak = 1
            else:
                #Check for daily habit
                if self.type == "daily":
                    #If user checked yesterday and is checking today, increase streak
                    if self.last_checked == today - datetime.timedelta(days=1):
                        self.current_streak += 1
                    #If user is checking today but did not check for yesterday, reset streak to 1
                    else:
                        self.current_streak = 1
                #Check for weekly habit
                elif self.type == "weekly":
                    #If user last checked was within 7 days and is checking today, increase streak
                    if self.last_checked >= today - datetime.timedelta(days=7):
                        self.current_streak += 1
                    #If user is checking today but last check was more than 7 days ago, reset streak to 1
                    else:
                        self.current_streak = 1

            #Update the record: the date of today becomes the date of the last checked
            self.last_checked = today

        #For the situation when the user says that the habit has NOT been done for today
        #Namely, checked_today is no
        else:
        #Resets the current streak and clears last checked date
            self.current_streak = 0
            self.last_checked = None


#habit = Habit("swimming","daily")
#habit.last_checked = datetime.date.today() - datetime.timedelta(days=1)
#habit.current_streak = 1
#habit.check_done(True)
#print(habit.current_streak, habit.last_checked)
