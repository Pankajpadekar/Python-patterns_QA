# The hollow triangle star pattern is a star pattern in the shape of the triangle made of stars but hollow.

# Follow these steps:

# You can see the pattern up there be sure to understand it. Stars are printed only in first last column of any row, except the last row.
# Run a nested loop where external loop runs for the size of triangle.
# Inside create internal loop. Inside it check if its first or last row then print only stars. If not print starts only at first and last column else print spaces.

# *
# **
# * *
# *  *
# *   *
# ******

while True:

    n = int(input("Enter the number : "))

    for i in range(1, n+1):

        for j in range(i):
            if j == 0 or j == i-1:
                print("*", end='')

            else:
                if i != n:
                    print(" ", end='')

                else:
                    print("*", end='')
        print()
