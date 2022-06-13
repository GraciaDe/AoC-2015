with open("gift dimensions.txt") as file:
    gifts = [dim.strip("\n") for dim in file.readlines()]


print(gifts)
