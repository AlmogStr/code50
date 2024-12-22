import sys

try:
    filename = sys.argv[1]
    if not filename.endswith('.py'):
        sys.exit("Not a Python file")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line argument")

    with open(filename, "r") as file:
        count = 0
        for line in file:
            if line.lstrip() != "\n" and not line.lstrip().startswith('#') and line.lstrip() != "":
                count += 1
        print(count)

except IndexError:
    sys.exit("Too few command-line arguments")
except FileNotFoundError:
    sys.exit("File not found")


