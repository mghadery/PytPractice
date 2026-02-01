def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #check length 2-6
    if not(2<=len(s)<=6):
        return False

    #check start with two characters
    if not("A"<=s[0:1]<="Z"):
        return False

    if not("A"<=s[1:2]<="Z"):
        return False

    #check all alphabetical
    #check numbers only at the end
    #the first digit cannot be 0
    dig_det = False
    for c in s:
        if not ("A"<=c<="Z" or "0"<=c<="9"):
            return False
        if "A"<=c<="Z" and dig_det:
            return False
        if not dig_det and c=="0":
            return False
        if not dig_det and "0"<=c<="9":
            dig_det = True
    return True


if __name__ == "__main__":
    main()

