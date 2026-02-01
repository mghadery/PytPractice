class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        s = ""
        for _ in range(self._size):
            s += "🍪"
        return s


    def deposit(self, n):
        self.check_int_nonneg(n)
        self.size += n

    def withdraw(self, n):
        self.check_int_nonneg(n)
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self.check_int_nonneg(value)
        self._capacity = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if (value < 0):
            raise ValueError("negative size")
        if (value>self._capacity):
            raise ValueError("capacity exceeded")
        self._size = value

    def check_int_nonneg(self, value):
        if type(value) != type(2):
            raise ValueError("non integer capacity")
        if (value<0):
            raise ValueError("negative capacity")

if __name__ == "__main__":
    jar = Jar(0)
    jar = Jar(4)
    print(jar)
    jar.deposit(3)
    print(jar)
    jar.deposit(2)
    print(jar)
    jar.withdraw(1)
    print(jar)

