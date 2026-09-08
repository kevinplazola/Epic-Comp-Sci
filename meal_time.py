def main():
    meal_time = input("What time is it? (HH:MM): ")
    converted_time = convert(meal_time)
    if 7 <= converted_time <= 8:
        return(str("breakfast time"))
    elif 12 <= converted_time <= 13:
        return(str("lunch time"))
    elif 18 <= converted_time <= 19:
        return(str("dinner time"))
    else:
        return(str(f"It's {meal_time}."))

def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + int(minutes) / 60
print(main())
