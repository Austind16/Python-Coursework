# Assignment operators

a,b,c,d,e = 1,2,3,4,7
a += 5 # Adding
b -= 5 # Subtracting
c *= 5 # Multiplying
d /= 5 # Dividing
e %= 5 # To find remainder
print(a)
print(b)
print(c)
print(d)
print(e)

print(15//2) # floor division

# Comparison operators

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a==b) # Check if equal or not
print(a!=b) # Check if not equal
print(a>b) # Check if greater to or not
print(a<b) # Check if smaller than or not
print(a>=b) # Check if greater than and equal or not
print(a<=b) # Check if smaller than and equal or not

# Logical operators

age = 21
Ind = False
print(age > 18 and Ind == True) 
print(age > 18 or Ind == True)
print(not age > 18)