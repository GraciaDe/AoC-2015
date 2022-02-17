with open("floor directions.txt") as file:
    floors = file.read()

a = 0
i = 0
for direction in floors:
    if direction == "(":
        a += 1
        i += 1
    elif direction == ")":
        a -= 1
        i += 1
    if a == -1:
        break

print(i)
