import random as rand

def main():
    while True:
        try:
            n = int(input("Level: "))
            l = range(1,n+1)
            choice = rand.choice(l)
        except ValueError:
            continue
        except IndexError:
            continue
        break

    while True:
        try:
            guess = int(input("Guess:"))
            if guess < 1:
                raise ValueError
        except ValueError:
            continue
        break

    if choice < guess:
        print("Too large!")
    elif choice > guess:
        print("Too small!")
    elif choice == guess:
        print("Just right!")

main()