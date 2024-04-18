Weight = float(input("Enter weight value: "))
unit_of_measurement = input(" is it in Kg or Lbs? (Type K for Kg an L for lbs) ")

# .upper() solves the issue of unit of measurement in lowercase
if unit_of_measurement.upper() == str('K'):
    convert = str(Weight * 2.205)
    print("Weight in lbs: " + convert)
elif unit_of_measurement.upper() == str("L"):
    convert = str(Weight // 2.205)
    print("Weight in kg: " + convert)
else:
    print("Unable to convert weight")
