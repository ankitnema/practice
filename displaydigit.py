# This program count the digit for the number input between 0-999
a = int(input("enter the number between 0-999 = "))
if a < 10:
    print(a, "It is a single digit number.")
elif a < 100:
    print(a, "is double digit number.")
elif a <= 999:
    print(a,"is 3 digit number.")
else:
    print(a," has invalid digits are not required for the program.")

