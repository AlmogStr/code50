def main():
    text = input("Input: ")
    output = ""
    for c in text:
        if c.lower() in ["a", "i", "o", "e", "u"]:
            continue
        else:
            output = output + c
    print(output)


if __name__ == '__main__':
    main()