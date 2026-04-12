with open("log.html", "r") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if "python" in line:
        print(f"Python is in the string, Line no. {lineno}")
        break
    lineno += 1

else:
    print("Python is not in the string")