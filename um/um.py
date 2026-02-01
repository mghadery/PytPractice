import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # Method 1
    # regex = r'^um[^a-z0-9]'
    # c = len(re.findall(regex, s, re.IGNORECASE))
    # regex = r'[^a-z0-9]um[^a-z0-9]'
    # c += len(re.findall(regex, s, re.IGNORECASE))
    # regex = r'[^a-z0-9]um$'
    # c += len(re.findall(regex, s, re.IGNORECASE))
    # regex = r'^um$'
    # c += len(re.findall(regex, s, re.IGNORECASE))

    # Method 2
    regex = r'\bum\b'
    c = len(re.findall(regex, s, re.IGNORECASE))

    return c


if __name__ == "__main__":
    main()
