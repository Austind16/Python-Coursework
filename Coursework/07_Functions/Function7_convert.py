# WAP for a function to convert farenheit to celcius
far = float(input("Enter degree in farenheit: "))
def convert(far):
    cel = ((far-32)*5)/9 # Calculating from farenheit to celsius
    print("Celsius = %.2F"%cel) # returns value only upto 2 decimal places
    return cel # return returns the value of cel

result = convert(far)
print(far, "farenheit in celcius is: ", result)