import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    regex = r'<iframe.*?src="https?://(?:www\.)?youtube\.com/embed/(\w+?)/?".*?></iframe>'
    m = re.search(regex, s, re.IGNORECASE)
    return 'https://youtu.be/' + m.group(1) if m else None


if __name__ == "__main__":
    main()
