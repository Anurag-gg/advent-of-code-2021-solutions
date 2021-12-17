from collections import defaultdict
import heapq

a = []
with open('day15/data.txt' ,'r') as data:
    for x in data:
        x = x.strip()
        if x:
            a.append(list(map(int ,list(x))))

row = len(a)*5
col = len(a[0])*5

def getWeight(r , c):
    value = (a[r%len(a)][c%len(a[0])] + (r//len(a)) + (c//len(a[0])))
    return (value - 1)%9+1



def dequeue(priority):
    #print(f"PRIORITY:{priority}")
    cost , x, y  = heapq.heappop(priority)
    return (cost , x,y)



def dijsktra(map , priority,done):
    while map[(row-1,col-1)] == 0:
        e = dequeue(priority)
        cost , x , y = e
        if (x,y) in done:
            continue
        done.add((x,y))
        map[(x,y)] = cost
        #for left
        if y-1>=0 and (x,y-1) not in done:
            heapq.heappush(priority , (cost + getWeight(x,y-1) , x ,y-1))
        #for right
        if y+1<=row-1 and (x,y+1) not in done:
            heapq.heappush(priority , (cost + getWeight(x,y+1) , x ,y+1))
        #for up
        if x-1>=0 and (x-1,y) not in done:
            heapq.heappush(priority , (cost + getWeight(x-1,y) , x-1 ,y))
        #for down
        if x+1<=col-1 and (x+1,y) not in done:
            heapq.heappush(priority , (cost + getWeight(x+1,y) , x+1 ,y))
    return map[(row-1,col-1)]


#           cost x y
priority = [(0,0,0)]
heapq.heapify(priority)
map = defaultdict(int)
map[(0,0)] = 0
print(dijsktra(map ,priority , set())) 