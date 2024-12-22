def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dt = d.replace("$", "")
    return float(dt)


def percent_to_float(p):
    pt = p.replace("%", "")
    return float(pt)/100


main()