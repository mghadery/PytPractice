import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        a = generate_integer(level)
        b = generate_integer(level)
        r = a + b
        errors = 0
        while True:
            try:
                ur = int(input(f"{a} + {b} = "))
                if r == ur:
                    score += 1
                    break
                else:
                    raise ValueError()
            except ValueError:
                print("EEE")
                errors += 1
                if errors >= 3:
                    print(f"{a} + {b} = {r}")
                    break

    print("Score:", score)


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n
        except ValueError:
            pass


def generate_integer(level):
    match level:
        case 1:
            return random.randint(0,9)
        case 2:
            return random.randint(10,99)
        case 3:
            return random.randint(100,999)
        case _:
            raise ValueError()

if __name__ == "__main__":
    main()
