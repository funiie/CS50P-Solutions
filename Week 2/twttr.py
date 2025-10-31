# Removes vowels from input text

# Prompt user for input
text = input("Input: ")

# Initialize empty string for result
twttr_text = ""

# Loop through each character and keep it only if it's not a vowel
for char in text:
    if char.lower() not in "aeiou":
        twttr_text += char

# Output the result
print(twttr_text)
