# Left triangle pattern
n = 5
for i in range(n+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()