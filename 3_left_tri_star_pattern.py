# The left triangle star pattern is a star pattern in the shape of a triangle. It is quite easy to create it.

# Steps to create a left triangle star pattern:
# Run a nested for loop where internal loop will run for number of times external loop has run.
# Print star in each iteration of internal loop.
# Print a new line at the end of internal loop.

# *
# **
# ***
# ****
# *****

while True:

    n = int(input("Enter the number : "))

    for i in  range(1,n+1):

        print("*" * (i))