def main():
    months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
    }
    try:
        date = input("Date: ").title()
        date = date.strip()
        if " " in date:
            month, day, year = date.split(" ")
            month = month.title()
            month = int(months[month])
            day = int(day[0:-1])
        elif "/" in date:
            month, day, year = date.split("/")
            month, day = int(month), int(day)
            if month > 12:
                main()
        else:
            main()

        if day > 31:
            main()

        print(year, f"{month:02}-{day:02}", sep = "-")

    except KeyError:
        main()

    except ValueError:
        main()


main()