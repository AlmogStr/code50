import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip):
        for _ in range(1,4):
            if 0 <= int(matches.group(_)) <= 255:
                continue
            else:
                return False
        return True
    else:
        return False
...


if __name__ == "__main__":
    main()
