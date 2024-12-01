"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
charge = 0.00
numChars = 8
color = "gold"
woodType = "oak"
# Charge for this sign.
# Number of characters.
if (numChars > 5):
    charge = (35 + (numChars-5)*4)
elif (numChars > 0):
    charge = 35
# Color of characters.
if (color == "gold"):
    charge += 15

# Type of wood.
if (woodType == "oak"):
    charge += 20

# Write assignment and if statements here as appropriate.

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
