from collections import defaultdict
d = defaultdict(int)
with open("day5/data.txt","r") as data:
    for x in data:
        initial , final = x.split("->")
        x1,y1 = map(lambda x : int(x.strip()),initial.split(","))
        x2,y2 = map(lambda x : int(x.strip()),final.split(","))
        for i in range(max(abs(y2-y1), abs(x2-x1))+ 1):
            x_temp = x1+i if x2>x1 else (x1-i if x1>x2 else x1)
            y_temp = y1+i if y2>y1 else (y1-i if y1>y2 else y1)
            d[(x_temp,y_temp)] += 1


print(sum([value>1 for value in d.values()]))
