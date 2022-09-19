##1 - 2/2! + 3/3! - 4/4! ....... +/- n/n!

n = int(input("Enter the value of n "))
sum = 0
i = 1
f = 1
sign = 1
while i<=n:
    f = f * i
    sum = sum + sign*i/f
    sign = sign * -1
    i = i + 1
print ("Sum is",sum)