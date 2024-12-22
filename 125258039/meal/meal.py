def main():
    mealtime = convert(input("What time is it? "))
    if 7 <= mealtime <= 8:
        print("breakfast time")
    elif 12 <= mealtime <= 13:
        print("lunch time")
    elif 18 <= mealtime <= 19:
        print("dinner time")


def convert(time):
    hour, minute = time.split(":")
    hour = float(hour)
    minute = float(minute)/60
    return hour + minute


if __name__ == "__main__":
    main()