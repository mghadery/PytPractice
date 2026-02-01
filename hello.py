print ("Hello world")
list = [1, 2, 3, 4, 5, 6]

#method 1
gen = (k for k in list if k % 2 == 0)
for k in gen:
    print(k)

#method 2
list2 = [k for k in list if k % 2 == 0]
for k in list2:
    print(k)

