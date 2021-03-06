## Promt user for a number and determine its length

value = 0

while value <= 0:
    number = input("Number: ")
    try:
        value = int(number)
    except:
        pass

print("Length:", len(number))


# while True:
#     number = input("Number: ")
#     try:
#         value = int(number)
#         if value > 0:
#             break
#     except:
#         pass
# print("Length:", len(number))
