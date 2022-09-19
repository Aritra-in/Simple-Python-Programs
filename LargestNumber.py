n1 = int(input("Enter number 1 "))
n2 = int(input("Enter number 2 "))
n3 = int(input("Enter number 3 "))

if n1>n2:
    if n1>n3:
        print (n1," is the largest")
    else:
        print (n3," is the largest")
else:
    if n2>n3:
        print (n2," is the largest")
    else:
        print (n3," is the largest")
print("End of the program")