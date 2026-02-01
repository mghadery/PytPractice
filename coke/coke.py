def pay(price):
    acceptedCoins = [5, 10, 25]
    paid = 0
    while paid < price:
        print("Amount Due:", price - paid)
        payment = int(input("Insert Coin:"))
        if payment in acceptedCoins:
            paid += payment
    print("Change Owed:", paid - price)

pay(50)
