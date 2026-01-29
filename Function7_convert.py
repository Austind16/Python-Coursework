# WAP for a function to convert farenheit to celcius
far = float(input("Enter degree in farenheit: "))
def convert(far):
    cel = ((far-32)*5)/9
    print("Celsius = %.2F"%cel)
    return cel

result = convert(far)
print(far, "farenheit in celcius is: ", result)