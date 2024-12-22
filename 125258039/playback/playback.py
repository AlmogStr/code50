def main():
    Original = input("Enter text with spaces for the magic to happen: ")
    Old = " "
    New = "..."
    Converted = Original.replace(Old, New)
    print(Converted)

main()