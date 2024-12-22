import sys
import csv
from tabulate import tabulate

try:
    filename = sys.argv[1]
    if not filename.endswith('.csv'):
        sys.exit("Not a CSV file")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    with open(filename, "r") as file:
        reader = csv.reader(file)
        print(tabulate(reader, headers="firstrow", tablefmt="grid"))


except IndexError:
    sys.exit("Too few command-line arguments")
except FileNotFoundError:
    sys.exit("File does not exist")
