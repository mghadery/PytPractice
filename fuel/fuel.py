def main():
    while True:
        try:
            percentage = convert(input("Fraction:"))
            g = gauge(percentage)
            print(g)
            break
        except (ValueError, ZeroDivisionError):
            continue


def convert(fraction):
    [x, y] = fraction.split("/")
    x = int(x)
    y = int(y)
    xdy = x / y
    if xdy > 1 or xdy < 0:
        raise ValueError
    percentage = round(100*xdy)
    return percentage


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
