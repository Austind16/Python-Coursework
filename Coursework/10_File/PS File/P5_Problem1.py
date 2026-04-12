f = open("poem.txt")

data = f.read()
data = data.lower()

if "twinkle" in data:
    print("The word twinkle is present in the file")
else:
    print("The word twinkle is not present in the file")
f.close()