for i in range(0, 10):
    for j in range(0, 100):
        if(j==0 or j==99 or i==0 or i==9):
            print("*", end='')
        else:
            print(" ",end='')
    print("")
