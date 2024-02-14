# The right downward triangle pattern is a pattern that is upside down and has perpendicular to the right side.

# Steps to create a right downward triangle pattern:

# From the above given pattern you can see that, this also requires 2 internal loop.
# First internal loop print spaces for i times and second internal loop print stars for size - i times.
# Here i is index of the current row.
# Print new line everytime after the internal loop.

#  ****
#   ***
#    **
#     *



while True:

    n = int(input("Enter the number : "))

    for i in range(n):

        print(" " * (i) + "*" * (n-i))