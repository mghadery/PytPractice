greeting = input("Greeting:").lower().strip()
if "hello" in greeting:  #not exact!
    payment = 0;
elif greeting.startswith("h"):
    payment = 20;
else:
    payment = 100;
print(f"${payment}")
