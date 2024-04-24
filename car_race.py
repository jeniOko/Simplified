HELP = """
  START - To start the car
  STOP - To stop the car
  QUIT - To exit
"""
START = " The car has started.....Ready to go"
STOP = " The car has stopped "
gamer = ""

# .upper() solves the case sensitive issue from user input
while gamer.upper() != 'QUIT':
    gamer = input("Game menu > ")
    if gamer.upper() == 'HELP':
        print(HELP)
    elif gamer.upper() == "START":
            print(START)
    elif gamer.upper() == "STOP":
            print(STOP)
    elif gamer.upper() == "QUIT":
        break
    else:
        print(" I don't understand that....")
