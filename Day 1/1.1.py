with open("floor directions.txt") as file:
    floors = file.read()

up = floors.count("(")
down = floors.count(")")

print(up - down)
