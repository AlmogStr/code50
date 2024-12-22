from pyfiglet import Figlet
import sys
import random

def main():

    figlet = Figlet()
    fonts = figlet.getFonts()
    accepted = ['-f', '-font']

    if len(sys.argv) == 3:
        if sys.argv[1] not in accepted:
            sys.exit("Invalid usage")

        f = sys.argv[2]
        if f not in fonts:
            sys.exit("Invalid usage")

        figlet.setFont(font=f)

    elif len(sys.argv) == 1:
        f = random.choice(fonts)
        figlet.setFont(font=f)

    else:
        sys.exit("Invalid usage")

    s = input("Input: ")
    print(figlet.renderText(s))


main()