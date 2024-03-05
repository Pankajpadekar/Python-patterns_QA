# The diamond star pattern is a star pattern with the shape of the diamond. You can see the pattern up here.

# If you look closely, you will see that the pattern is a combination of a pyramid pattern and a downward triangle star pattern. So you can create this pattern by combining both patterns.

# Here is the code to create this pattern.

#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

while True:

    n = int(input("Enter the number : "))

    for i in range(1, n+1):


        print(" " * (n-i) + "*" * (2*i-1) )


    for i in range(n+1):

        print(" " * i + "*" * (n-i) + "*" * (n-(i-1)) + " " * i  )


