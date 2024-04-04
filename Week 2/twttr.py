#prompt user for input
word = str(input("Input: "))
vowels = ["A","E","I","O","U","a","e","i","o","u"]

# out str with all vowels ommitted
for v in vowels:
    if v in word:
        word = word.replace(v, "")

print("output:", word)
