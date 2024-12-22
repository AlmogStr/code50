import sys
import csv

try:
    filename = sys.argv[1]
    outputname = sys.argv[2]
    if not filename.endswith('.csv'):
        sys.exit("Not a CSV file")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        with open(outputname, 'w') as output:
            writer = csv.DictWriter(output, fieldnames=['first', 'last', 'house'])
            writer.writeheader()
            for row in reader:
                last, first= str(row['name']).split(', ')
                writer.writerow({'first': first, 'last': last, 'house': row['house']})

except IndexError:
    sys.exit("Too few command-line arguments")
except FileNotFoundError:
    sys.exit("Could not read invalid_file.csv")
