# The hollow square pattern is a bit more difficult pattern program than a simple square because here you will have to deal with spaces within the square.

# Here are the steps to create a hollow square pattern.

# To create hollow pattern again run a nested for loop.
# External loop will be same as the previous square pattern but inside internal loop you will have to check the condition.
# If its the first or last row or column then print only stars.
# Otherwise check if its the first or last column then print star else print spaces.

# *****
# *   *
# *   *
# *   *
# *****

while True:

    n = int(input("Enter the number : "))

    for i in range(n):

        if i == 0 or i == n-1:
            print("*" * n)

        else:
            print("*" + " " * (n-2) + "*")