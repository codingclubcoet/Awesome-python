# Prints the below pattern
#   ******
#   ******
#   ******
#   ******
#   ******

for i in range(0, 5):
    print("")
    for j in range(0, 5):
        print("*", end='')
        # We use an extra end parameter in print as the default parameter is \n,
        #and normally the print statement at the end moves to the next line