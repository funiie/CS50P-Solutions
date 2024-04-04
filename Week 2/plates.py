def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# function
def is_valid(s):

    # max of 6 characters, min 2 characters
    if len(s) <= 6 and len(s) >= 2 and s[0:2].isalpha() and s.isalnum:

    # numbers cant be use in middle, used at first or last
        for char in s:
            if char.isdigit():
                position = s.index(char)
                if s[position:].isdigit() and int(char) != 0:
                    return True
                else:
                    return False
        return True
main()
