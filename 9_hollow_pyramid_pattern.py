# The hollow pyramid pattern is a pyramid pattern made of stars but hollow. You can see the pattern up there.

# Follow these steps to create hollow pyramid pattern:

# You can observe that we have to handle spaces at 2 different places. First before printing star and second between the pyramid.
# Create nested loop with 2 internal loops. First loop just create space, second loop print both spaces & stars with some logics.
# The first internal loop print spaces for size - i times.
# The second internal loop pexecutes for 2 * i - 1 times and checks if it is first or last row then print star, if not check if it is first or last column then print star else print space.

#     *
#    * *
#   *   *
#  *     *
# *********

while True:

    n = int(input("Enter the number : "))

    for i in range(1, n+1):

        print("*" + " " * (i) + "*")