# letter k 
n = 5 
for i in range(0,n-1):
    for j in range(0,n):
        if i ==n or i+j == n-1 or j == 0 :
            print("* " ,end = " ")
        else:
            print(" ",end=" ")
    print()   
n = 5 
for i in range(0,n):
    for j in range(0,n):
        if i ==j or i == n+1 or j == 0 :
            print("* " ,end = " ")
        else:
            print(" ",end=" ")
    print()  