# Write a python program to compute simple interest
p = float(input("Enter principal amount: ")) # principal amount
r = float(input("Enter rate of interest: ")) # rate of interest
n = float(input("Enter time period: ")) # Time period
i = (p*r*n)/100 # interest calculation
a = p+i # Maturity amount calculation
print("Simple interest is: ", i)
print("Maturity amount is: ", a)