print("Enter Marks that you have recieved in all five of your subjects")
Markone = int(input())
Marktwo = int(input())
Markthree = int(input())
Markfour = int(input())
Markfive = int(input())
Total = Markone+Marktwo+Markthree+Markfour+Markfive
avg = Total/5
if avg>=91:
    print("Your grade is A")
if avg>=81 and avg<=90:
    print("Your grade is a B")
if avg>=71 and avg<=80:
    print("Your grade is C")
if avg>=61 and avg<=70:
    print("Your grade is D")
if avg>=51 and avg<60:
    print("Your grade is F")