import random

while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except ValueError:
        pass


m = random.randint(1, n)

while True:
    try:
        k = int(input("Guess: "))
        if k > m:
            print("Too large!")
        elif 0 < k < m:
            print("Too small!")
        elif k == m:
            print("Just right!")
            break
    except ValueError:
        pass


