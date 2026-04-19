a = int(input("Enter Your Age: "))

# If elif else ladder

if(a>=18):
    print("Your are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are entering an invalid age")

elif(a==0):
    print("You are entering 0. Which is not valid age")


else:
    print("You are below the age of consent")



print("End of program")