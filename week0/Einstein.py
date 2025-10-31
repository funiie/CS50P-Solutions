# Calculate energy from mass using E = mc^2

# Prompt the user for mass in kilograms
mass = int(input("Enter mass in kg: "))

# Speed of light in meters per second
c = 300_000_000  

# Calculate energy in Joules
energy = mass * c * c

# Print the result
print(energy)

