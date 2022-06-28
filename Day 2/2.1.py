with open("gift dimensions.txt") as file:
    gifts = [box.strip("\n") for box in file.readlines()]

dimensions = [gift.split("x") for gift in gifts]
total = 0

for lwh in dimensions:
    a = int(lwh[0]) * int(lwh[1])
    b = int(lwh[0]) * int(lwh[2])
    c = int(lwh[1]) * int(lwh[2])

    total += (2*a) + (2*b) + (2*c) + min(a, b, c)

print(total)
