#Step 1: take user input
#Step 2: detect vowels
#Step 3: omit vowels

twitter = input("Input: ")
vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

for c in twitter:
    if c in vowels:
        pass
    else:
        print(c, end = "")