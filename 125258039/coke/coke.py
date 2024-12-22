def main():
    amount_due = 50

    while(amount_due > 0):
        print("Amount Due:", amount_due)
        coin = int(input("Insert Coin: "))
        if coin in [5,10,25]:
            amount_due = amount_due - coin

    print("Change Owed:", -amount_due)


if __name__ == '__main__':
    main()