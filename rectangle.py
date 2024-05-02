def area():
    if length < width:
        print("invalid measurements for a rectangle")
    else:
        area = length * width
        print(f'The area is : {area}')
        return area


def perimeter():
    if length < width:
        print("invalid measurements for a rectangle")
    else:
        perimeter = 2 * (length + width)
        print(f'The perimeter is : {perimeter}')
        return perimeter


# Get length and width from the user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
action = input("\nACTION LIST \n P for perimeter\n A for Area\n B for Both area and perimeter\n Select action >")


if action.upper() == 'P':
    perimeter()
  
elif action.upper() == 'A':
    area()
  
elif action.upper() == 'B':
    area()
    perimeter()
  
else:
    print("Cannot recognize action. Reload and input correct action")
