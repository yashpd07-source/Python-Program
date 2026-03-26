n = int(input("Enter a whole number: "))
binary = 0
place = 1
while n > 0:
    remainder = n % 2
    binary += remainder * place
    place *= 10
    n //= 2
print("Binary:", binary)