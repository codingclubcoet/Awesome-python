# Prints the following pattern
#   1                   1
#   12                 21
#   123               321
#   ......          .....
#   .......        ......
#   123.......nn......321
#   n<=9

n = int(input("Enter n :\t"))
space = n*2-2
for i in range(1, n + 1):
    for j in range(1, i+1):
        print(j, end='')
    for k in range(0, space):
        print(" ", end='')
    for l in range(i, 0, -1):
        print(l, end='')
    print("")
    space=space-2
