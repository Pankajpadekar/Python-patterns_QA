# The pyramid pattern is a very famous pattern in programming. It has the shape of an equilateral triangle and it is used to represent a pyramid. You can see the pattern up here.

# The pyramid pattern has an odd number of stars in each row 1, 3, 5, 7, etc.

# Again we need to nest the loops.
# Create 2 internal loop, first print spaces and second print stars.
# Print spaces for number of times equal to size - i and stars for 2 * i - 1 times.
# Here i is the current row.

#     *
#    ***
#   *****
#  *******
# *********

while True:

    n = int(input("Enter the number : "))

    for i in range(1,n+1):

        print(" " * (n-i) + "*" * (2*i-1))