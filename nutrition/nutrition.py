def get_fruit_col(fruit):
    col_tab = {
        "apple":130,
        "avocado": 50,
        "banana":110,
        "cantaloupe": 50,
        "grapefruit":60,
        "grapes":90,
        "honeydew melon":50,
        "kiwifruit": 90,
        "lemon":15,
        "lime":20,
        "nectarine":60,
        "orange":80,
        "peach":60,
        "pear":100,
        "pineapple":50,
        "plums":70,
        "strawberries":50,
        "sweet cherries":100,
        "tangerine":50,
        "watermelon":80
    }
    return col_tab[fruit] if fruit in col_tab else -1

fruit = input("Item: ").lower()
col = get_fruit_col(fruit)
if col != -1:
    print("Colories:", col)
