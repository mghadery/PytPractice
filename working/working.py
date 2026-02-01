import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    #input
    # 9:00 AM to 5:00 PM
    # 9 AM to 5 PM
    # 9:00 AM to 5 PM
    # 9 AM to 5:00 PM

    #output
    #9:00 to 17:00

    regex = r'(^\d{1,2})(?::(\d{1,2}))? +([AP])M to (\d{1,2})(?::(\d{1,2}))? +([AP])M$'
    m = re.search(regex, s)
    if not m:
        raise ValueError("Format Error")

    h1 = int(m.group(1))
    m1 = int(m.group(2)) if m.group(2) else 0
    p1 = m.group(3) == 'P'
    h2 = int(m.group(4))
    m2 = int(m.group(5)) if m.group(5) else 0
    p2 = m.group(6) == 'P'

    # print(h1)
    # print(m1)
    # print(h2)
    # print(m2)

    if h1 > 12 or h2 > 12 or m1 > 59 or m2 > 59:
        raise ValueError("Range Error")

    if p1:
        if h1 != 12:
            h1 += 12
    else:
        if h1 == 12:
            h1 = 0

    if p2:
        if h2 != 12:
            h2 += 12
    else:
        if h2 == 12:
            h2 = 0

    return f'{h1:02}:{m1:02} to {h2:02}:{m2:02}'


if __name__ == "__main__":
    main()
