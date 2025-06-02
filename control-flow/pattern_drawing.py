# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop to iterate over rows
while row < size:
    # Use for loop to print '*' size times in the current row
    for _ in range(size):
        print("*", end="")
    print()  # Newline after each row
    row += 1