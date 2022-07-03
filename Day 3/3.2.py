with open("delivery route.txt") as file:
    directions = file.read()

santa_x, robo_x = 0, 0
santa_y, robo_y = 0, 0

coord = [(0,0)]

# Santa's intstructions
for santa_point in directions[::2]:
    if santa_point =="<":
        santa_x -= 1
    elif santa_point ==">":
        santa_x += 1
    elif santa_point in "vV":
        santa_y -= 1
    elif santa_point =="^":
        santa_y += 1
    
    if (santa_x,santa_y) not in coord:
        coord.append((santa_x,santa_y))

# Robo's intstructions
for robo_point in directions[1::2]:
    if robo_point =="<":
        robo_x -= 1
    elif robo_point ==">":
        robo_x += 1
    elif robo_point in "vV":
        robo_y -= 1
    elif robo_point =="^":
        robo_y += 1
    
    if (robo_x,robo_y) not in coord:
        coord.append((robo_x,robo_y))

print(len(coord))