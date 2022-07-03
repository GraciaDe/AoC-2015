with open("delivery route.txt") as file:
    directions = file.read()


x = 0
y = 0

coord = [(0,0)]

for point in directions:
    if point =="<":
        x -= 1
    elif point ==">":
        x += 1
    elif point in "vV":
        y -= 1
    elif point =="^":
        y += 1
    
    if (x,y) not in coord:
        coord.append((x,y))

print(len(coord))