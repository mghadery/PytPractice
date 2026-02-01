def get_item_price(item):
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    try:
        item = item.title()
        return menu[item]
    except KeyError:
        raise ValueError("Item Not found")

price = 0
try:
    while True:
        item = input("Item: ")
        try:
            price += get_item_price(item)
            print(f"${price:.2f}")
        except ValueError:
            pass

except EOFError:
    print("")


