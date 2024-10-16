# The reverse pyramid pattern is the same as the pyramid pattern but it is upside down. See the pattern up there.

# Just like the pyramid pattern, the reverse pyramid pattern follows the same logic. The only difference is that we have to print the spaces and stars with reverse logic.

# *********
#  *******
#   *****
#    ***
#     *

while True:

    n = int(input("Enter the number : "))

    for i in range (1,n+1):

        print(" " * i + "*" * (n-i) + "*" * (n-(i-1)) + " " * i )