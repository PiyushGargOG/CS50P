# step 1 is ask user for input
# step 2 is check capital letters one by one
# step 3 is convert that into snake case

camelcase = input("camelCase? ")
for c in camelcase:
    if c.isupper():
        print("_" + c.lower(), end="")
    else:
        print(c, end = "")