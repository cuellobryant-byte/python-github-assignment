print("Welcome to my Savings Goal Tracker!")
goal = input("What is your savings goal amount? ")
weekly_savings = input("How much do you save per week? ")
try:
    goal = float(goal)
    weekly_savings = float(weekly_savings)
    if weekly_savings == 0:
        print("Weekly savings cannot be zero.")
        exit()
except ValueError:
    print("Please enter valid numbers.")
    exit()

weeks_needed = goal / weekly_savings
print(f"It will take approximately {weeks_needed:.1f} weeks to reach your savings goal.")
