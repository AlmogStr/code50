import emoji

def main():


    userinput = input("Input: ")
    if "_" not in userinput:
        print(emoji.emojize('Output: ' + userinput, language='alias'))
    else:
        print(emoji.emojize('Output: ' + userinput))



main()