def main():
    s = convert(input("Give me your chat text:"))
    print(f"Your emoji rich text: {s}")

def convert(str):
    return str.replace(":)", "🙂").replace(":(", "🙁")

main()
