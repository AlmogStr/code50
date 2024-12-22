def convert(phrase):
    converted = phrase.replace(":)","🙂")
    converted = converted.replace(":(","🙁")
    return converted


def main():
    original = input("Enter text with emotion: ")
    print(convert(original))


main()