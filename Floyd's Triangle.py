rows = int(input("Please enter the total number of rows you would like to have: "))
number = 1
print("Floyd's Triangle Style!")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(number, end =' ')
        number = number + 2
    print()