with open("check1.txt", "r") as f:
    data1 = f.read()

with open("check2.txt", "r") as f:
    data2 = f.read()

if (data1 == data2):
    print("Yes both the files are identical")
else:
    print("No both the files are not identical")