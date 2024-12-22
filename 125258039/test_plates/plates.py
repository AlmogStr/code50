def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return (is_long(s) & begin_w_letter(s) & no_num_in_middle(s) & only_nums_letters(s))


def is_long(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False


def begin_w_letter(s):
    if s[0:2].isalpha():
        return True
    else:
        return False


def no_num_in_middle(s):
    flag = 0
    for c in s:
        if c.isalpha() and flag == 0:
            continue
        elif c == '0' and flag == 0:
            return False
        elif c.isdigit():
            flag = 1
        else:
            return False
    return True


def only_nums_letters(s):
    for c in s:
        if c.isalnum():
            continue
        else:
            return False
    return True


if __name__ == "__main__":
    main()