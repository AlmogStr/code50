def main():
    d = {}
    while(True):
        try:
            item = input().upper()
            if item not in d:
                d.update({item: 1})
            else:
                d[item] = d[item] + 1
        except EOFError:
            for c in sorted(d):
                value = str(d[c])
                print(value + " " + c)
            break


main()