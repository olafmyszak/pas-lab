filename = input("Enter file name: ")
file = open("lab1zad1.png", "wb")

with open(filename, "rb") as f:
    while True:
        byte = f.read(1)
        if not byte:
            break
        file.write(byte)
