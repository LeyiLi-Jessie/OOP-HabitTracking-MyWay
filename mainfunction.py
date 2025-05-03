from tracker import Tracker

# Initialize the tracker
tracker = Tracker()

#Main menu function
def app_menu():
    while True:
        print("\nHabit Tracker - MyWay Menu")
        print("1. Add a new habit")
        print("2. Delete a habit")
        print("3. List all habits")
        print("4. Check off a habit")
        print("5. Show habit with highest streak")
        print("6. Show streak of a specific habit")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Please enter the name of the new habit:")
            type = input("Please enter the type of the new habit (either daily or weekly):")
            tracker.add_habit(name, type)
            print("The new habit is added. Please select option 3 to view all habits.")
        elif choice == '2':
            name = input("Please enter the habit name to delete it: ")
            tracker.delete_habit(name)
            print("Habit is delete. Please select option 3 to view remaining habits.")
        elif choice == '3':
            habits = tracker.list_habits()
            for habit in habits:
                print(f"Name: {habit[0]}, Streak: {habit[3]}")
        elif choice == '4':
            name = input("Enter habit name to check off: ")
            checked_today = input("Did you finish the habit today? (yes/no): ").lower() == 'yes'
            tracker.check_habit(name, checked_today)
            print("Checked successfully! Please select option 3 to view.")
        elif choice == '5':
            top = tracker.highest_streak()
            if top:
                print(f"Habit with highest streak: {top[0]} - {top[1]} days")
        elif choice == '6':
            name = input("Enter habit name: ")
            streak = tracker.streak_of_habit(name)
            if streak:
                print(f"{name}'s current streak: {streak[0]} days")
        elif choice == '7':
            print("Thank you for using MyWay. See you next time!")
            break
        else:
            print("Invalid option. Try again.")

#Predefined habits of the app.
def predefined_habits():
    tracker.create_table()
    tracker.add_habit(f"drinking 2L water", "daily")
    tracker.add_habit(f"jogging", "weekly")
    tracker.add_habit(f"writing journal", "daily")
    tracker.add_habit(f"swimming", "weekly")
    tracker.add_habit(f"gardening", "weekly")

if __name__ == "__main__":
        predefined_habits()
        app_menu()