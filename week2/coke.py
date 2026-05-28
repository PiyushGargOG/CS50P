#step 1: set price of coke to be 50 cents
#step 2: ask user to insert a coin
#step 3: if amount is less than 50 the ask user to again insert a coin using loop till collection of 50 cents
#step 4: if amount is greater than 50 then ask user to collect extra amount and print extra amount

print("Amount Due: 50")
price  = int(50)
total = 0
valid = [5, 10, 25]

while True:
    insert = int(input("Insert Coin: "))
    if insert not in valid:
        print("Amount Due: 50")
        continue
    total = total + insert
    print(f"Amount Due: {price - total}")
    if total < price:
        continue
    elif total > price:
        print(f"Change Owed: {total - price}")
        break
    elif total == price:
        print("Change Owed: 0")
        break