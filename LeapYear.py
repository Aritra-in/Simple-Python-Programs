n = int(input("Enter a year "))

if n%4!=0:
    print("Not a Leap Year")
else:
    if n%100==0:
        if n%400==0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year")