def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if not (len(s) >= 2 and len(s) <= 6 and s[0:2].isalpha()):
        return False

    if not s.isalnum():
        return False

    number_started = False
    for char in s:
        if char.isdigit():
            number_started = True
        if number_started and char.isalpha():
            return False

    for char in s:
        if char.isdigit():
            if char == "0":
                return False
            break

    return True


main()