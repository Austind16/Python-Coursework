r = float(input("Enter your radius: ")) #input() function takes input from user and returns it as a string. We need to convert it to float using float() function.
a = 3.14*r**2 #** is the exponentiation operator in Python. It raises the number to the power of the exponent. In this case, it raises r to the power of 2.
c = 2*3.14*r # * is the multiplication operator in Python. It multiplies the two numbers. In this case, it multiplies 2, 3.14 and r to get the circumference of the circle.
print("Area of circle is: ", a)
print("Circumference of circle is: ", c)