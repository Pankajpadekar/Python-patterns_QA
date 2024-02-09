# The left downward triangle pattern is the star pattern of a triangle upside down. It is very easy to create.

# Run 2 nested loops where the internal loop will run size - i times and external loop will run size times. Here i is the current row.

# *****
# ****
# ***
# **
# *

while True:

    n = int(input("Enter the number : "))

    for i in range(n):

        print("*" * ((n-i)))