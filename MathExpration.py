## 1+ 1/x + 1/x*x + ...

x = int(input("Enter the value of x "))
n = int(input("Enter the value of n "))
sum = 1
i = 1
while i<=n:
    sum = sum + 1/x**i
    i = i + 1
print("Sum is",sum)