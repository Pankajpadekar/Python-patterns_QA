# The square pattern is the easiest pattern program. It is a pattern that has the shape of a square made of stars.

# Let's see how to create and print a square pattern.

# Take size of the square as input from the user or just set a value.
# Run a nested loop for the number of rows and columns.
# Print the star in each iteration and print a new line after each row.

# *****
# *****
# *****
# *****
# *****

while True:

    n = int(input("Enter the number : "))

    for i in range(n):

        print("*" * n)