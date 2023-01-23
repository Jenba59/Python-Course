print ("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm? "))
if height <= 120:
    print("Sorry you can't ride😣, but you can try los carritos chocones!😀")
else:
    age = int(input("What is your age? "))
    if age < 12:
        price = 5
    elif age >= 12 and age < 18:
        price = 7
    elif age >= 45 and age < 55:
        price = 0
        print ('Enjoy the rest of your life 💀')
    else:
        price = 12
    photos = input("Do you want photos taken? Y or N ").upper()
    if photos == 'Y':
        price += 3
    print("The total bill is $" + str(price))