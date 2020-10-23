r,c=map(int,input().split())
row=[]
num=1
for i in range(r):
    column=[]
    for j in range(c):
        column.append(num)
        num+=1
    row.append(column)    
        
a=1
for i in range(r):
    b=1
    for j in range(c):
        if(b<c):
            print(row[i][j],end=" ")
            b+=1
            continue
        print(row[i][j],end='')
    if(a<r):
        print()
        a+=1
