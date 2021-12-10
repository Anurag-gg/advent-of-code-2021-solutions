a = []
with open("day9/data.txt" , "r") as data:
    for x in data:
        temp = list(x)
        a.append(list(map(int , temp[:-1])))


result = 0
for row in range(len(a)):
    for col in range(len(temp)-1):
        cell = a[row][col]
        if row > 0:
            if not cell < a[row-1][col]:
                continue
        if col > 0:
            if not cell < a[row][col-1]:
                continue
        if row+1 < len(a):
            if not cell < a[row+1][col]:
                continue
        if col+1 < len(temp)-1:
            if not cell < a[row][col+1]:
                continue
        result += 1 + cell

print(result)