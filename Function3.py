def function3(child3, child2, child1):
    # Printing the name of the youngest child
    # Since we are passing arguments by keyword,
    # the order of arguments while calling the function does not matter
    print("The youngest child is: ", child3)

# Calling the function using keyword arguments
# This makes the code more readable and avoids confusion with parameter order
function3(child1 = "Johnny", child2 = "Alex", child3 = "Benji")