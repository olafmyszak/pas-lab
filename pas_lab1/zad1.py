filename = input("Enter file name: ")

with open(filename, "r") as firstfile, open("lab1zad1", "w") as secondfile:
    for line in firstfile:
        secondfile.write(line)
