temp = float(input("What is the temperature in Fahrenheit? "))
if temp < 60:
    print("You need to bring a sweater.")
elif temp >= 140:
    print("Invalid input, you'd be dead.")
else:
    print("You do not need to bring a sweater.")