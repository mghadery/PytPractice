def make_snake_case(s):
    res = ""
    ind = 0
    first_ind = 0
    for ind in range(len(s) + 1):
        c = s[ind] if ind < len(s) else ""
        if ind == len(s) or "A"<=c<="Z":
            if res != "":
                res += "_"
            res += s[first_ind: ind].lower()
            first_ind = ind
        ind += 1
    return res

s = input("camelCase:").strip()
print(make_snake_case(s))
