import random as rand

def main():
    score = 0
    n = get_level()
    for i in range(0,10):
        x = generate_integer(n)
        y = generate_integer(n)
        j = 0
        while j<3:
            print(x, "+", y, "=", end=" ")
            try:
                answer = int(input())
                if answer != (x+y):
                    raise ValueError
                else:
                    score += 1
                    break
            except ValueError:
                print("EEE")
                j += 1
                continue
        if j==3:
            print(x, "+", y, "=", x+y)
    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level < 4:
                return level
            else:
                raise ValueError
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return rand.choice(range(0,10))
    elif level == 2:
        return rand.choice(range(10,100))
    else:
        return rand.choice(range(100,1000))


if __name__ == "__main__":
    main()