from data import a

horizontal , depth = 0 , 0
for element in a:
    direction , distance = element.split()
    if direction == "forward":
        horizontal += int(distance)
    elif direction == "down":
        depth += int(distance)
    elif direction == "up":
        depth -= int(distance)
print(horizontal * depth)