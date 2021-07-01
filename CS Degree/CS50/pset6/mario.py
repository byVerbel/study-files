height = 0

while height > 8 or height < 1:
    height = int(input("Height: "))

spaces = height - 1

for i in range(height):
    for j in range(height):
        if j < spaces - i:
            print(" ", end="")
        else:
            print("#", end="")

    print("  ", end="")

    for k in range(i + 1):
        print("#", end="")

    print("")
