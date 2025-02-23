# The codes below calculates for leap year.

print("Welcome to a leap year calculator!")
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print("Not leap year")
    else:
        print(f"{year} is a leap year")
else:
    print("Not leap year")