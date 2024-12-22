def main():
    camel_case = input("camelCase: ")
    snake_case = ""
    for c in camel_case:
        if c.islower():
            snake_case = snake_case + c
        elif c.isupper():
            snake_case = snake_case + "_" + c.lower()
    print(snake_case)


if __name__ == '__main__':
    main()