
bill_amount = float(input("Enter the bill amount: "))
payment = float(input("Enter the payment amount: "))
due = bill_amount - payment
if due > 0:
    print(f"Amount still due: ${due:.2f}")
elif due < 0:
    print(f"Change to return: ${-due:.2f}")
else:
    print("The bill is fully paid. No balance remaining.")