# This function has a default parameter value
# If no argument is passed while calling the function,
# the default value "India" will be used
def function4(country = "India"): 
    print("I am from: ", country)

function4("Sweden") # Calling the function with an argument, this will override the default value
function4() # Calling the function without any argument, the default value "India" will be used
function4("America") # Calling the function with an argument, this will override the default value once again

# def function4(country = "India", name): # Python does not allow a non-default argument (name) after a default argument (country).


def function4(name, country = "India"): 
# This function takes two parameters:
# name → required parameter (must be provided)
# country → optional parameter with a default value "India"
    print("I am from: ", country)
    print("My name is: ", name)

function4("Billy","Sweden") # Calling the function with both arguments, this overrides the default country value
function4("Billy") # Calling the function with only the required argument, the default country "India" will be used automatically