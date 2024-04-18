temperature = int(input("What is the temperature in degree Celsius : "))

if temperature > 57:# Highest world temperature record in celsius
    print("That temperature is higher")
    print("Ensure it is in degree celsius")
elif temperature > 30:
    print("It is a hot day")
    print("drink plenty of water")
elif temperature > 20: #btwn 20 and 30
    print("It is a warm day")
    print("enjoy the weather")
elif temperature > 15: #btwn 15 & 20
    print("It is a cool day")
    print("Put on warm clothes")
else:
    print("It is freezing")
