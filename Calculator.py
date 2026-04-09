def add(A, B):
    return A + B
def subtract(A, B):
    return A - B
def multiply(A, B):
    return A * B
def divide(A, B):
    return A / B
print("Please select the operation.")
print("A. Add")
print("B. Subtract")
print("C. Multiply")
print("D.Divide")
choice = input("Please enter choice (a,b,c,d): ")
num_1 = int(input("Please enter the first number: "))
num_2 = int(input("Please enter the second number: "))
if choice =='a':
    print (num_1, "+", num_2, " = ", add(num_1, num_2))
elif choice == 'b':
    print (num_1, "-", num_2, " = ", subtract(num_1, num_2))
elif choice =='c':
    print (num_1, "*", num_2, " = ", multiply(num_1, num_2))
elif choice == 'd':
    print (num_1, "/", num_2, " = ", divide(num_1, num_2))
else:
    print("Your input is invalid.")