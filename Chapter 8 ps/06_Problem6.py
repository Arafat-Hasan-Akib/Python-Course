def inch_to_cms(inch):
    return inch * 2.54

n = int(input("Enter the length in inches: "))
print(f"{n} inches is equal to {round(inch_to_cms(n), 2)} centimeters.")