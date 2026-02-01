import validators

mail = input("What's your email address? ")

r = validators.email(mail)

print ("Valid") if r else print("Invalid")
