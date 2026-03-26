print("Half Pyramid of Stars (*):")
n = int(input("Enter the number of rows you would like: "))
for i in range(n):
    for j in range(i+1):
        print("* ")
    print()