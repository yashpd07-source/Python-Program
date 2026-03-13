print("Welcome to the Uber app!")
print("Select your ride:")
print("1.Bike")
print("2.Car")
choice = int(input("Enter your choice!"))
if( choice == 1 ):
    print("What type of bike?")
    print("1. The Bullet")
    print("2. GT-650")
    choice2 = int(input("Enter your choice!"))
    if choice2 ==1:
        print("You havce selected The Bullet!")
    else:
        print("You have selected GT-650!")
elif( choice == 2 ):
    print("What type of car would you like to ride in!")
    print("1. Buggati Bolide")
    print("2. Mustang 1969")
    choice3 = int(input("Enter your choice!"))
    if choice3 == 1:
        print("you have chosen Buggati Bolide!")
    else:
        print("You have selected Mustang 1969!")
else:
    print("Wrong choice.")
print("-Hand crafted by Yash Deshpande!!!!!!!!")                       