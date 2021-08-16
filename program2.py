flag = 0
print("Enter the total number of locks")
locks = int(input(" "))
if (locks <= 0) or (locks > 70):
    flag = 1
print("Enter the total number of stocks")
stocks = int(input(" "))
if (stocks <= 0) or (stocks > 80):
    flag = 1
print("Enter the total number of barrels")
barrels = int(input(" "))
if (barrels <= 0) or (barrels > 90):
    flag = 1
if flag == 1:
    print("invalid input")
    exit(0)
t_sales = (locks * 45) + (stocks * 30) + (barrels * 25)
if t_sales <= 1000:
    commission = 0.10 * t_sales

elif t_sales < 1800:
    commission = 0.10 * 1000
    commission = commission + (0.15 * (t_sales - 1000))

else:
    commission = 0.10 * 1000
    commission = commission + (0.15 * 800)
    commission = commission + (0.20 * (t_sales - 1800))

print("The total sales is", t_sales)
print(" The commission is", commission)
