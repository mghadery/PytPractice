def main():
    greeting = input("Greeting:")
    payment = value(greeting)
    print(f"${payment}")

def value(greeting):
    greeting = greeting.lower().strip()
    if greeting.startswith("hello"):  #not exact!
        payment = 0;
    elif greeting.startswith("h"):
        payment = 20;
    else:
        payment = 100;
    return payment


if __name__ == "__main__":
    main()



