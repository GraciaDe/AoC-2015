with open("gift dimensions.txt") as file:
    gifts = [box.strip("\n") for box in file.readlines()]

dimension_string = [gift.split("x") for gift in gifts]
dimensions = []

for dim_str in dimension_string:
    for i in range(3):
        dim_str[i] = int(dim_str[i])

    dimensions.append(dim_str)

ribbon = 0
mini = []

for dim in dimensions:
    base = dim[0]*dim[1]*dim[2]
    dim.remove(max(dim))
    extra = 2*(dim[0]+dim[1])

    ribbon += base + extra

print(ribbon)