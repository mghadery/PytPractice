def main():
    inp = input("Input:")
    print(f"Output: {shorten(inp)}")


def shorten(word):
    vowels = ['a', 'o', 'u', 'e', 'i']
    s = ""
    for c in word:
        if c.lower() not in vowels:
            s += c
    return s


if __name__ == "__main__":
    main()
