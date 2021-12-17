from collections import defaultdict
import math

a = []
with open('day15/data.txt' ,'r') as data:
    for x in data:
        x = x.strip()
        if x:
            a.append(list(map(int ,list(x))))

row = len(a)
col = len(a[0])
result = [[0 for _ in range(col)]for _ in range(row)]

def dequeue(priority , done):
    low = min([x for x in priority.values()])
    for key , value in priority.items():
        if value == low:
            priority.pop(key)
            done.append(key)
            x , y = key
            result[x][y] = value
            return key



def dijsktra(priority,done):
    while result[row-1][col-1] == 0:
        e = dequeue(priority , done)
        x , y = e
        present_value = result[x][y]
        #for left
        if y-1>=0 and (x,y-1) not in done:
            priority[(x,y-1)] = min(priority[(x,y-1)] , present_value + a[x][y-1] )
        #for right
        if y+1<=row-1 and (x,y+1) not in done:
            priority[(x,y+1)] = min(priority[(x,y+1)] , present_value + a[x][y+1] )
        #for up
        if x-1>=0 and (x-1,y) not in done:
            priority[(x-1,y)] = min(priority[(x-1,y)] , present_value + a[x-1][y] )
        #for down
        if x+1<=col-1 and (x+1,y) not in done:
            priority[(x+1,y)] = min(priority[(x+1,y)] , present_value + a[x+1][y] )
    return result[row-1][col-1]




q = defaultdict(lambda:math.inf)
q[(0,0)] = 0
print(dijsktra(q , []))