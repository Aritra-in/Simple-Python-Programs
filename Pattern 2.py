n=int(input("Enter the number of lines: "))
for i in range (1,n+1):
    for j in range (1,n+1):
        if(j==1 or j==n):
            print("*",end=" ") 
        else:
            if(i==1 or i==n):
                print("*",end=" ")
            else:
                print(" ",end=" ")
            print(end=" ")
    print()                                                                                                                                               