with open("day7/data.txt","r") as data:
    for x in data:
        a = list(map(int ,str(x).split(",")))


a.sort()
median = a[len(a)//2]
print(sum([abs(e-median) for e in a]))