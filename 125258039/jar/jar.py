class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        howmuch = ""
        for _ in range(self.size):
            howmuch = howmuch + "🍪"
        return howmuch

    def deposit(self, n):
        jar = self.size
        jar = jar + n
        if jar > self.capacity:
            raise ValueError("Too many cookies")
        self.size = jar
        return self.size

    def withdraw(self, n):
        jar = self.size
        jar = jar - n
        if jar < 0:
            raise ValueError("Too less cookies")
        self.size = jar
        return self.size

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not capacity > 0:
            raise ValueError("Invalid Capacity")
        self._capacity = capacity


    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError("Empty jar")
        self._size = size

def main():
    try:
        usercap = int(input("Define capacity: "))
    except ValueError:
        usercap = 12
    jar = Jar(capacity = usercap)
    while(True):
        action = input("Choose action (d or w): ")
        if action not in ["d","w"]:
            raise ValueError("Invalid action")
        n = int(input("How many cookies: "))
        if action == "d":
            jar.deposit(n)
        elif action == "w":
            jar.withdraw(n)
        print(jar)

#main()
