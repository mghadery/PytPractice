import inflect

names = []
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print()
        break

p = inflect.engine()
print("Adieu, adieu, to", p.join(names, conj="and"))
