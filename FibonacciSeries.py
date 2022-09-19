n = int(input("Enter a number: "))
n1=0
n2=1
print(n1,end=" ")
print(n2,end=" ")
i=1
while(i<=n-2):
    n3=n1+n2
    n1=n2
    n2=n3
    i=i+1
    print(n3,end=" ")
print()