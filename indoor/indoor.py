def main():
    yell = input("You can yell now:")
    indoorVoice = makeIndoor(yell)
    print("This is your indoor voice:", indoorVoice)

def makeIndoor(yell):
    return yell.lower()

main()
