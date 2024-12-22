from datetime import date
from datetime import timedelta
import inflect
import sys


def main():
    ...
    date_string = input("What's your date of birth? (YYYY-MM-DD) ")
    try:
        days = howmanydaysdoilive(date_string)
    except ValueError:
            sys.exit("Invalid date")
    days = days.capitalize() + " minutes"
    print(days)
...

def howmanydaysdoilive(date_string):
    birthdate = date.fromisoformat(date_string)
    datetoday = date.today()
    deltatime = date.__sub__(datetoday, birthdate)
    days = deltatime.days
    minutes = days * 24 * 60
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")
    return words


if __name__ == "__main__":
    main()
