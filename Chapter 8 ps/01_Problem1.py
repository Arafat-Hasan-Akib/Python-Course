a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b    
    elif(c>a and c>b):
        return c
    

print("The greatest number is: ", greatest(a, b, c))