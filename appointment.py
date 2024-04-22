from datetime import date

# Get user's name
name = input("Hello, Welcome to our online guest book \n  What is your name? ")

# Get today's date
today = date.today()
print(f"Hello, {name}! Today's date is {today.strftime('%B %d, %Y')}")

appointments = ["2024-04-23 : At 10:00AM Appointment 1", "2024-04-23 : At 1:00PM Appointment 2"]#examples of appointments

# Check for appointments today
has_appointments = False
for appointment in appointments:
  if today.strftime('%Y-%m-%d') in appointment:
    has_appointments = True
    print(appointment)
if not has_appointments:
  print("You don't have any appointments today but you can book with us")
