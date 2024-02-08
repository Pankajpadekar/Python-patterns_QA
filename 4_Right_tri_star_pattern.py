# The right triangle star pattern is a star pattern in the shape of a triangle as shown above. It is similar to the left triangle star pattern but you will have to deal with spaces.

# Steps to create a right triangle star pattern:

# Create a loop that will run for the number of rows (size).
# Inside this we will have 2 loops, first will print spaces and second will print stars. (look at pattern above)
# Spaces will be printed for size - i times and stars will be printed for i times. Where i is the current row.
# Print new line at the end of both internal loops

#     *
#    **
#   ***
#  ****
# *****

while True:

    n = int(input("Enter the number : "))

    for i in range(1,n+1):

        print(" " * (n-i) + "*" * i)