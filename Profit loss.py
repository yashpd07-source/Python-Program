actual_cost = int(input("Enter the actual product price:"))
sale_cost = int(input("Enter the sales amount:"))
if (sale_cost > actual_cost):
    amount = sale_cost - actual_cost
    print("Total profit is:",amount)
else:
    print("No Profit")
    