def main():
    text = input("Input: ")
    output = shorten(text)
    print(output)


def shorten(word):
    output = ""
    for c in word:
        if c.lower() in ["a", "i", "o", "e", "u"]:
            continue
        else:
            output = output + c
    return output


if __name__ == "__main__":
    main()