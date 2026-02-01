import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if not (match := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)):
        return False

    ip = [int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))]
    #print ([x for x in ip if x > 255])
    return False if [x for x in ip if x > 255] else True




if __name__ == "__main__":
    main()
