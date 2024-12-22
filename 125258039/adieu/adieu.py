import inflect

def main():

    p = inflect.engine()
    l = []

    while(True):
        try:
            s = input("Name: ")
            l = l + [s]

        except EOFError:
            break
    mylist = p.join(l)
    print("\nAdieu, adieu, to" , mylist)

main()