from collections import defaultdict
d = defaultdict(int)
with open("day5/data.txt","r") as data:
    for x in data:
        initial , final = x.split("->")
        x1,y1 = map(lambda x : int(x.strip()),initial.split(","))
        x2,y2 = map(lambda x : int(x.strip()),final.split(","))
        if x1-x2 == 0:
            for i in range(abs(y1-y2)+ 1):
                d[tuple(*[(x1,y1+i) if y2-y1>0 else (x1,y1-i)])] += 1
        elif y1-y2 == 0:
            for i in range(abs(x1-x2)+ 1):
                d[tuple(*[(x1+i,y1) if x2-x1>0 else (x1-i,y1)])] += 1

print(sum([value>1 for value in d.values()]))
