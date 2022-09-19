n = int(input("Enter a number: "))
i=1
f=0
while(i<=n):
    if (n%i==0):
        f+=1
    i=i+1
if(f==2):
    print("Prime Number")
else:
    print("Not Prime Number")