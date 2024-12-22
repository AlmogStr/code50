import re
import sys

def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit("ValueError")

def convert(s):
    try:
        matches = re.search(r"^([0-9]{1,2}):?([0-5][0-9])? (AM|PM) to ([0-9]{1,2}):?([0-5][0-9])? (PM|AM)$", s)
        if matches == None:
            raise ValueError

        hour1 = int(matches.group(1))
        if hour1 > 12:
            raise ValueError

        min1 = matches.group(2)
        if min1 == None:
            min1 = 0
        else:
            min1 = int(min1)
        if min1 > 59:
            raise ValueError

        meridiem1 = matches.group(3)
        if meridiem1 == "PM":
            if hour1 == 12:
                hour1 = 12
            else:
                hour1 = hour1 + 12
        else:
            if hour1 == 12:
                hour1 = 0

        hour2 = int(matches.group(4))
        if hour2 > 12:
            raise ValueError

        min2 = matches.group(5)
        if min2 == None:
            min2 = 0
        else:
            min2 = int(min2)
        if min2 > 59:
            raise ValueError

        meridiem2 = matches.group(6)
        if meridiem2 == "PM":
            if hour2 == 12:
                hour2 = 12
            else:
                hour2 = hour2 + 12
        else:
            if hour2 == 12:
                hour2 = 0

    except ValueError:
        raise ValueError

    return f"{hour1:02}:{min1:02} to {hour2:02}:{min2:02}"


if __name__ == "__main__":
    main()
