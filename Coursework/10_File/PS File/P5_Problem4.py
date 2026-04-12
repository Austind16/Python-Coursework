words = ["Donkey", "Bad", "Ganda", "Dirty", "Explicit"]

with open("Censor.txt", "r") as f:
    data = f.read()

for word in words:
    data = data.replace(word, "#" * len(word))

with open("Censor.txt", "w") as f:
    f.write(data)