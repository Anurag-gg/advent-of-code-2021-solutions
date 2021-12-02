from data import a

horizontal , depth , aim = 0,0,0
for element in a:
    direction , distance = element.split()
    if direction == "forward":
        horizontal += int(distance)
        depth += aim*int(distance)
    elif direction == "down":
        aim += int(distance)
    elif direction == "up":
        aim -= int(distance)
print(horizontal * depth)
