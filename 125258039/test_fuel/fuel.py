def main():
    try:
        fraction = input("Fraction: ")
        percentage = convert(fraction)
        print(gauge(percentage))

    except ValueError:
        main()
    except ZeroDivisionError:
        main()

def convert(fraction):
    X, Y = fraction.split("/")
    if int(Y) == 0:
        raise ZeroDivisionError
    elif int(X) > int(Y):
        raise ValueError
    else:
        percentage = round((int(X)/int(Y))*100)
        return percentage

def gauge(percentage):
    if 1 < percentage < 99:
        return str(percentage) + "%"
    elif percentage <= 1:
        return "E"
    elif 99 <= percentage <= 100:
        return "F"


if __name__ == "__main__":
    main()