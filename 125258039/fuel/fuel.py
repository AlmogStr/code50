def main():
    try:
        X, Y = input("Fraction: ").split("/")
        percentage = round((int(X)/int(Y))*100)
        if 1 < percentage < 99:
                print(str(percentage) + "%")
        elif percentage <= 1:
            print("E")
        elif 99 <= percentage <= 100:
            print("F")
        else:
            main()
    except ValueError:
        main()
    except ZeroDivisionError:
        main()


main()