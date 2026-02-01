def main():
    items = get_dic()
    print()
    print_dic(items)

def get_dic():
    items = {}
    while True:
        try:
            item = input().lower()
        except EOFError:
            return items
        if item in items:
            items[item] += 1
        else:
            items[item] = 1

def print_dic(items):
    sorted_items = sorted(items)
    for item in sorted_items:
        print(items[item], item.upper())

main()


